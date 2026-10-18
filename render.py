import sys,os,subprocess,math
from multiprocessing import Pool
from playwright.sync_api import sync_playwright
FPS=30;OUT='/home/claude/lj/frames';os.makedirs(OUT,exist_ok=True)
URL='file:///home/claude/lj/index.html?render=1'
def work(rng):
    with sync_playwright() as p:
        b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080});pg.goto(URL);pg.evaluate('window.ready')
        for f in range(*rng):
            pg.evaluate(f'render({min(f/FPS,pg_total)})') if False else pg.evaluate(f'render({f/FPS})')
            pg.screenshot(path=f'{OUT}/f{f:05d}.jpg',type='jpeg',quality=94)
        b.close()
if __name__=='__main__':
    with sync_playwright() as p:
        b=p.chromium.launch();pg=b.new_page();pg.goto(URL);T=pg.evaluate('TOTAL');b.close()
    n=int(round(T*FPS));k=int(sys.argv[1]) if len(sys.argv)>1 else 2;ch=math.ceil(n/k)
    print('frames',n,'dur',T,flush=True)
    with Pool(k) as P:P.map(work,[(i*ch,min(n,(i+1)*ch)) for i in range(k)])
    subprocess.run(['ffmpeg','-y','-framerate',str(FPS),'-i',OUT+'/f%05d.jpg','-c:v','libx264','-pix_fmt','yuv420p','-crf','17','-preset','medium','-movflags','+faststart','/home/claude/lj/LittleJoys_onboarding_landscape.mp4'],check=True,capture_output=True)
    print('done',flush=True)
