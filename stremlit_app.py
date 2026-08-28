import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ساعة مواقيت الصلاة",
    page_icon="🕌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
.block-container {padding: 0 !important; max-width: 100% !important;}
[data-testid=\"stAppViewContainer\"] {background:#071006;}
iframe {border:0 !important;}
</style>
""", unsafe_allow_html=True)

HTML = r'''
<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="theme-color" content="#071006">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="ساعة المسجد">
<meta name="format-detection" content="telephone=no">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<title>ساعة مواقيت الصلاة</title>
<style>
:root{--gold:#ffd21a;--bg:#071006;--panel:#10200f;--panel2:#0b170a;--muted:#cfd7ca;--green:#42ff55;--orange:#ffae22}
*{box-sizing:border-box}html,body{margin:0;min-height:100%;background:var(--bg);color:#fff;font-family:Tahoma,"Segoe UI",Arial,sans-serif}
body{display:flex;justify-content:center;padding:max(8px,env(safe-area-inset-top)) 8px max(8px,env(safe-area-inset-bottom))}
.frame{width:min(100%,860px);min-height:calc(100vh - 12px);border:3px double var(--gold);border-radius:22px;padding:8px;background:radial-gradient(circle at 50% 10%,#163319 0,#0b190b 42%,#071006 100%);display:flex;flex-direction:column;gap:11px}
.headerBox{border:2px solid var(--gold);border-radius:0 0 20px 20px;padding:4px 7px 3px;position:relative;background:rgba(7,20,8,.58);text-align:center}
.headerBox:before,.headerBox:after{content:"";position:absolute;top:9px;width:42px;height:18px;border-top:2px solid var(--gold)}.headerBox:before{right:18px}.headerBox:after{left:18px}
.title{font-size:clamp(22px,4.8vw,36px);font-weight:800;line-height:1.08;text-align:center;width:100%}.mosqueName{font-size:clamp(17px,3.8vw,28px);font-weight:800;color:var(--gold);margin-top:2px;text-align:center;width:100%}.mosqueLine{display:flex;align-items:center;gap:12px;justify-content:center;margin-top:5px;color:var(--gold)}.mosqueLine .line{height:2px;width:26%;background:linear-gradient(90deg,transparent,var(--gold),transparent)}.mosqueIcon{font-size:25px}.location{font-size:clamp(12px,2.8vw,18px);margin-top:1px;color:#f4f4f4;text-align:center;width:100%}
.clockBox{background:#000;border:2px solid var(--gold);border-radius:18px;padding:5px 7px 4px;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:104px}
.clockTime{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:clamp(36px,8.5vw,60px);font-weight:900;letter-spacing:1px;line-height:.96}.ampm{font-size:clamp(18px,4.5vw,32px);font-weight:800;line-height:1;margin-top:2px}.date{color:var(--gold);font-size:clamp(14px,3vw,20px);font-family:ui-monospace,monospace;margin-top:5px}
.prayers{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;flex:1}
.card{border:2px solid var(--gold);border-radius:15px;background:rgba(18,42,18,.78);min-height:116px;padding:5px 4px 4px;display:flex;flex-direction:column;align-items:center;justify-content:center;transition:.2s}.card.active{border-color:#fff000;background:linear-gradient(135deg,#8f8200,#d9c600 55%,#827600);box-shadow:0 0 0 3px #fff000,0 0 28px rgba(255,240,0,.95),inset 0 0 24px rgba(255,255,80,.42)}.card.active .name,.card.active .time,.card.active .period,.card.active .iqVal,.card.active .iqama{color:#111}.card.active .iqBtn{border-color:#111;color:#111;background:#ffe733}.name{font-size:clamp(18px,4vw,27px);font-weight:800;color:var(--gold);margin-bottom:8px}.time{font-family:ui-monospace,monospace;font-size:clamp(23px,5.3vw,36px);font-weight:900;line-height:1}.period{font-size:clamp(16px,4vw,26px);font-weight:800;margin-top:4px}.iqama{font-size:clamp(12px,2.4vw,16px);color:#e9ece6;margin-top:7px;white-space:nowrap}.iqControls{display:flex;align-items:center;justify-content:center;gap:7px;margin-top:7px}.iqBtn{width:26px;height:26px;border:1.5px solid var(--gold);border-radius:50%;background:#071006;color:var(--gold);font-size:19px;font-weight:900;line-height:20px}.iqVal{font-weight:800;min-width:28px}.noIqama{height:37px}
.countdowns{border:2px solid var(--gold);border-radius:17px;display:grid;grid-template-columns:1fr 1fr;background:rgba(18,42,18,.76);overflow:hidden}.countCell{padding:7px 5px;text-align:center;min-height:82px;display:flex;flex-direction:column;justify-content:center}.countCell+ .countCell{border-right:1px solid var(--gold)}.countTitle{color:var(--gold);font-weight:800;font-size:clamp(16px,3.8vw,25px);margin-bottom:4px}.countValue{font-family:ui-monospace,monospace;font-size:clamp(23px,5.2vw,38px);font-weight:900}.adhanLeft{color:var(--orange)}.iqamaLeft{color:var(--green)}.blink{animation:blink 1s linear infinite}@keyframes blink{50%{opacity:.25}}
.toolbar{display:flex;gap:8px;justify-content:center;flex-wrap:wrap}.toolBtn{border:1.5px solid var(--gold);border-radius:11px;background:#132212;color:var(--gold);padding:8px 13px;font-weight:800;font-size:14px}.toolBtn.on{background:var(--gold);color:#111}.status{text-align:center;color:#c7d1c2;font-size:12px;min-height:16px;padding-bottom:1px}

.settingsBox{display:none;border:1.5px solid var(--gold);border-radius:12px;padding:8px;background:rgba(9,24,9,.92);gap:7px;grid-template-columns:1fr 1fr}.settingsBox.show{display:grid}.settingsBox input{width:100%;border:1px solid #5f774f;border-radius:9px;background:#071006;color:#fff;padding:8px;font-size:14px}.settingsBox button{grid-column:1/-1;border:1.5px solid var(--gold);border-radius:9px;background:var(--gold);color:#111;padding:7px;font-weight:900}
@media(max-width:520px){.frame{gap:8px;padding:9px;border-radius:20px}.headerBox{padding:7px 7px 5px}.clockBox{min-height:112px}.prayers{gap:7px}.card{min-height:132px}.iqBtn{width:28px;height:28px}.countCell{min-height:94px}}
@media(max-height:780px) and (max-width:520px){.headerBox{padding:5px 6px 4px}.mosqueLine{margin-top:3px}.mosqueIcon{font-size:27px}.clockBox{min-height:104px;padding:5px}.card{min-height:116px;padding:5px 4px}.name{margin-bottom:5px}.iqama{margin-top:4px}.iqControls{margin-top:4px}.countCell{min-height:82px;padding:6px}.toolbar{gap:5px}.toolBtn{padding:6px 9px;font-size:12px}}

/* تعديل أخير: تصغير معتدل بحوالي 10% فقط */
@media(max-width:520px){
  .headerBox{padding:6px 6px 4px}
  .title{font-size:clamp(20px,4.3vw,32px)}
  .mosqueName{font-size:clamp(15px,3.4vw,25px)}
  .mosqueLine{margin-top:4px}
  .mosqueIcon{font-size:23px}
  .location{font-size:clamp(11px,2.5vw,16px)}
  .clockBox{min-height:101px;padding:4px 6px}
  .prayers{gap:6px}
  .card{min-height:119px;padding:4px 4px 3px}
  .name{font-size:clamp(16px,3.6vw,24px);margin-bottom:6px}
  .time{font-size:clamp(21px,4.8vw,32px)}
  .period{font-size:clamp(14px,3.6vw,23px);margin-top:3px}
  .iqama{font-size:clamp(11px,2.2vw,14px);margin-top:6px}
  .iqControls{margin-top:6px;gap:6px}
  .iqBtn{width:24px;height:24px;font-size:17px}
  .noIqama{height:33px}
  .countCell{min-height:85px;padding:6px 4px}
  .countTitle{font-size:clamp(14px,3.4vw,22px)}
  .countValue{font-size:clamp(21px,4.7vw,34px)}
  .toolBtn{padding:7px 11px;font-size:13px}
  .status{font-size:11px;min-height:14px}
}


/* تعديل 21: تصغير خفيف إضافي قرابة 5% للارتفاع فقط */
.frame{gap:calc(11px * .95);padding:calc(8px * .95)}
.headerBox{padding:3.8px 7px 2.85px}
.clockBox{min-height:99px;padding:4.75px 7px 3.8px}
.card{min-height:110px;padding:4.75px 4px 3.8px}
.name{margin-bottom:7.6px}
.iqama{margin-top:6.65px}.iqControls{margin-top:6.65px}
.countCell{min-height:78px;padding:6.65px 5px}
.toolBtn{padding:7.6px 12.35px}
@media(max-width:520px){.frame{gap:7.6px;padding:8.55px}.headerBox{padding:6.65px 7px 4.75px}.clockBox{min-height:106px}.card{min-height:125px}.countCell{min-height:89px}}
@media(max-height:780px) and (max-width:520px){.headerBox{padding:4.75px 6px 3.8px}.clockBox{min-height:99px;padding:4.75px}.card{min-height:110px;padding:4.75px 4px}.countCell{min-height:78px;padding:5.7px}.toolBtn{padding:5.7px 8.55px}}


/* تعديل 22: تقليل الفراغ داخل مستطيلات أوقات الصلاة فقط
   بدون تغيير العرض، مع تكبير الخط للاستفادة من المساحة */
.card{
  min-height:104px;
  padding:1px 4px;
}
.name{
  font-size:clamp(19px,4.2vw,28px);
  margin-bottom:3px;
}
.time{
  font-size:clamp(24px,5.5vw,37px);
}
.period{
  font-size:clamp(16px,4.1vw,26px);
  margin-top:1px;
}
.iqama{
  font-size:clamp(12px,2.5vw,16px);
  margin-top:3px;
}
.iqControls{
  margin-top:3px;
  gap:6px;
}
.iqBtn{
  width:24px;
  height:24px;
}
.noIqama{
  height:26px;
}

@media(max-width:520px){
  .card{
    min-height:108px;
    padding:1px 4px;
  }
  .name{
    font-size:clamp(18px,4vw,26px);
    margin-bottom:3px;
  }
  .time{
    font-size:clamp(23px,5.2vw,35px);
  }
  .period{
    font-size:clamp(15px,3.9vw,24px);
    margin-top:1px;
  }
  .iqama{
    font-size:clamp(12px,2.4vw,15px);
    margin-top:3px;
  }
  .iqControls{
    margin-top:2px;
  }
  .noIqama{
    height:24px;
  }
}

/* تعديل 23: تقصير مستطيلات أوقات الصلاة وإزالة الفراغ الداخلي فقط */
.card{min-height:94px;padding:0 4px}
.name{margin-bottom:1px}
.iqama{margin-top:1px}
.iqControls{margin-top:1px}
.noIqama{height:20px}
@media(max-width:520px){
  .card{min-height:96px;padding:0 4px}
  .name{margin-bottom:1px}
  .iqama{margin-top:1px}
  .iqControls{margin-top:1px}
  .noIqama{height:18px}
}
@media(max-height:780px) and (max-width:520px){
  .card{min-height:94px;padding:0 4px}
}


/* تعديل 23: تقليل الفراغ أسفل أزرار الإقامة فقط، دون تغيير الأزرار أو النص */
.card{
  justify-content:flex-start;
  min-height:96px;
  padding-top:1px;
  padding-bottom:0;
}
@media(max-width:520px){
  .card{
    min-height:98px;
    padding-top:1px;
    padding-bottom:0;
  }
}

/* تعديل 24: منع شبكة أوقات الصلاة من التمدد رأسيًا، مع إبقاء النص في المنتصف */
.prayers{
  flex:0 0 auto;
  align-content:start;
}
.card{
  justify-content:center;
  min-height:0;
  padding-top:1px;
  padding-bottom:1px;
}
@media(max-width:520px){
  .prayers{flex:0 0 auto;align-content:start}
  .card{justify-content:center;min-height:0;padding-top:1px;padding-bottom:1px}
}


/* تعديل 25: مسافة قصيرة ومتوازنة أسفل أزرار الإقامة */
.prayers{flex:none;}
.card{
  min-height:112px;
  padding:4px 4px 7px;
  justify-content:center;
}
@media(max-width:520px){
  .prayers{flex:none;}
  .card{
    min-height:114px;
    padding:4px 4px 7px;
    justify-content:center;
  }
}
@media(max-height:780px) and (max-width:520px){
  .card{
    min-height:112px;
    padding:3px 4px 6px;
    justify-content:center;
  }
}

/* تعديل 26: رفع الحد السفلي للإطار الخارجي فقط لإزالة الفراغ أسفل المحتوى */
.frame{min-height:0;height:auto;}
@media(max-width:520px){.frame{min-height:0;height:auto;}}


/* تعديل 30: تكبير عداد الإقامة + الملاحظات والتنبيهات + اتجاه القبلة */
.countCell.iqamaRunning{
  background:rgba(26,70,22,.82);
  min-height:118px;
}
.countCell.iqamaRunning .countTitle{
  font-size:clamp(20px,4.8vw,32px);
}
.countCell.iqamaRunning .countValue{
  font-size:clamp(42px,10vw,64px);
  line-height:1;
  letter-spacing:1px;
}
.utilityPanel{
  display:none;
  border:1.5px solid var(--gold);
  border-radius:14px;
  padding:10px;
  background:rgba(9,24,9,.96);
}
.utilityPanel.show{display:block}
.utilityPanel h3{margin:0 0 9px;color:var(--gold);text-align:center;font-size:20px}
.utilityGrid{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.utilityPanel input,.utilityPanel textarea,.utilityPanel select{
  width:100%;border:1px solid #5f774f;border-radius:9px;background:#071006;color:#fff;padding:9px;font-size:16px
}
.utilityPanel textarea{min-height:86px;resize:vertical;grid-column:1/-1}
.utilityActions{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:8px}
.utilityAction{
  border:1.5px solid var(--gold);border-radius:10px;background:var(--gold);color:#111;
  padding:8px 12px;font-weight:900;font-size:15px
}
.utilityAction.secondary{background:#132212;color:var(--gold)}
.noteList{margin-top:10px;display:grid;gap:7px}
.noteItem{border:1px solid #5f774f;border-radius:10px;padding:8px;background:#071006}
.noteMeta{font-size:12px;color:#cfd7ca;margin-top:5px}
.noteText{font-size:16px;font-weight:700;white-space:pre-wrap}
.noteBtns{display:flex;gap:6px;margin-top:6px}
.noteBtns button{border:1px solid var(--gold);background:#132212;color:var(--gold);border-radius:8px;padding:5px 8px}
.qiblaWrap{text-align:center}
.qiblaCompass{
  width:190px;height:190px;margin:8px auto 12px;border:3px solid var(--gold);border-radius:50%;
  position:relative;background:radial-gradient(circle,#173518 0,#071006 68%)
}
.qiblaCompass::before{content:"N";position:absolute;top:7px;left:50%;transform:translateX(-50%);color:#fff;font-weight:900}
.qiblaArrow{
  position:absolute;left:50%;top:50%;width:8px;height:76px;background:var(--gold);
  transform-origin:50% 100%;transform:translate(-50%,-100%) rotate(0deg);border-radius:8px 8px 2px 2px
}
.qiblaArrow::before{
  content:"";position:absolute;top:-13px;left:50%;transform:translateX(-50%);
  border-left:12px solid transparent;border-right:12px solid transparent;border-bottom:18px solid var(--gold)
}
.qiblaInfo{font-size:18px;font-weight:800}
.qiblaSmall{font-size:13px;color:#cfd7ca;margin-top:5px}
@media(max-width:520px){
  .countCell.iqamaRunning{min-height:124px}
  .countCell.iqamaRunning .countTitle{font-size:clamp(22px,5.5vw,34px)}
  .countCell.iqamaRunning .countValue{font-size:clamp(48px,12vw,70px)}
  .utilityGrid{grid-template-columns:1fr}
}


/* ===== التصميم المعتمد النهائي ===== */
@media (max-width:520px){
  body{
    padding:max(4px,env(safe-area-inset-top)) 4px max(4px,env(safe-area-inset-bottom));
  }
  .frame{
    width:100%;
    max-width:100%;
    gap:6px;
    padding:6px;
    border-radius:18px;
    min-height:0;
  }
  .headerBox{padding:4px 6px 3px}
  .title{font-size:clamp(19px,4.1vw,29px)}
  .mosqueName{font-size:clamp(15px,3.2vw,23px)}
  .mosqueLine{margin-top:2px}
  .mosqueIcon{font-size:20px}
  .location{font-size:clamp(11px,2.3vw,15px)}

  .clockBox{
    min-height:92px;
    padding:4px 6px;
  }
  .clockTime{font-size:clamp(34px,7.8vw,54px)}
  .ampm{font-size:clamp(16px,4vw,26px)}
  .date{font-size:clamp(13px,2.7vw,18px);margin-top:3px}

  .prayers{gap:5px}
  .card{
    min-height:104px;
    padding:3px 3px 5px;
  }
  .name{font-size:clamp(17px,3.7vw,24px);margin-bottom:2px}
  .time{font-size:clamp(22px,5vw,33px)}
  .period{font-size:clamp(14px,3.5vw,22px)}
  .iqama{font-size:clamp(11px,2.2vw,14px);margin-top:2px}
  .iqControls{margin-top:2px;gap:5px}
  .iqBtn{width:22px;height:22px;font-size:15px;line-height:18px}
  .noIqama{height:18px}

  .countdowns{border-radius:14px}
  .countCell{
    min-height:74px;
    padding:5px 4px;
  }
  .countTitle{font-size:clamp(14px,3.3vw,20px);margin-bottom:2px}
  .countValue{font-size:clamp(21px,4.8vw,32px)}

  /* عند عمل العد التنازلي للإقامة تكون واضحة جدًا */
  .countCell.iqamaRunning{
    min-height:104px;
  }
  .countCell.iqamaRunning .countTitle{
    font-size:clamp(20px,5vw,30px);
  }
  .countCell.iqamaRunning .countValue{
    font-size:clamp(46px,11.5vw,68px);
    line-height:.95;
  }

  /* الأزرار السفلية المعتمدة: صغيرة ومتقاربة */
  .toolbar{
    gap:5px;
    flex-wrap:nowrap;
    align-items:stretch;
  }
  .toolBtn{
    padding:5px 7px;
    font-size:12px;
    min-height:34px;
    border-radius:9px;
    white-space:nowrap;
  }
  #enableAdhan{
    flex:1 1 auto;
  }
  #editMosque,#notesBtn,#qiblaBtn{
    flex:0 1 auto;
    min-width:0;
  }
  .status{
    font-size:10px;
    min-height:12px;
    line-height:1.2;
    padding-bottom:0;
  }
}

/* للشاشات القصيرة جدًا */
@media (max-width:520px) and (max-height:700px){
  .frame{gap:4px;padding:5px}
  .headerBox{padding:3px 5px 2px}
  .clockBox{min-height:84px}
  .card{min-height:96px;padding:2px 3px 4px}
  .countCell{min-height:68px}
  .toolBtn{padding:4px 6px;font-size:11px;min-height:31px}
}

/* تعديل 31 المعتمد: توسيع منطقتي العدادات والأزرار السفلية لاستغلال الفراغ */
@media (max-width:520px){
  .countdowns{grid-template-columns:1fr 1fr;}
  .countCell{min-height:92px;padding:8px 5px;}
  .countTitle{font-size:clamp(16px,3.8vw,23px);margin-bottom:4px;}
  .countValue{font-size:clamp(24px,5.5vw,37px);}
  .toolbar{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;width:100%;}
  .toolBtn,#enableAdhan,#editMosque,#notesBtn,#qiblaBtn,#calendarBtn,#adhkarBtn,#fridayBtn{width:100%;min-width:0;min-height:46px;padding:7px 3px;font-size:12px;display:flex;align-items:center;justify-content:center;}
}


/* ===== تحسينات نسخة الجوال ===== */
html{
  -webkit-text-size-adjust:100%;
  text-size-adjust:100%;
  overscroll-behavior:none;
}
body{
  min-height:100dvh;
  min-height:-webkit-fill-available;
  touch-action:manipulation;
  -webkit-tap-highlight-color:transparent;
}
button,input,select,textarea{font:inherit}
button{touch-action:manipulation;cursor:pointer}
.toolBtn,.iqBtn,.utilityAction{user-select:none;-webkit-user-select:none}
@media (max-width:520px){
  body{align-items:flex-start}
  .frame{
    min-height:calc(100dvh - max(8px,env(safe-area-inset-top)) - max(8px,env(safe-area-inset-bottom)));
  }
  .toolbar{position:relative;z-index:2}
  .toolBtn{font-weight:900}
  .iqBtn{min-width:30px;min-height:30px}
  .utilityPanel{max-height:72dvh;overflow:auto;-webkit-overflow-scrolling:touch}
  .settingsBox input,.utilityPanel input,.utilityPanel textarea,.utilityPanel select{font-size:16px}
}
@media (orientation:landscape) and (max-height:520px){
  body{padding:3px}
  .frame{gap:4px;padding:5px}
  .headerBox{padding:2px 5px}
  .mosqueLine{display:none}
  .clockBox{min-height:68px}
  .clockTime{font-size:clamp(30px,7vw,48px)}
  .date{margin-top:1px}
  .card{min-height:86px}
  .countCell{min-height:68px;padding:4px}
  .toolbar{gap:4px}
  .toolBtn{min-height:36px;padding:4px 2px;font-size:11px}
}

/* تعديل 27-08-2026: مطابقة أدق لأم القرى + تمديد بسيط من أسفل على الجوال */
@media (max-width:520px){
  body{padding-bottom:max(2px,env(safe-area-inset-bottom));}
  .frame{min-height:calc(100dvh - max(4px,env(safe-area-inset-top)) - max(2px,env(safe-area-inset-bottom)));}
}

</style>
</head>
<body>
<div class="frame">
  <div class="headerBox">
    <div class="title">ساعة مواقيت الصلاة</div>
    <div class="mosqueName" id="mosqueName">اسم المسجد</div>
    <div class="mosqueLine"><span class="line"></span><span class="mosqueIcon">🕌</span><span class="line"></span></div>
    <div class="location" id="locationText">📍 جاري تحديد الموقع…</div>
  </div>

  <div class="clockBox">
    <div class="clockTime" id="clock">--:--:--</div>
    <div class="ampm" id="ampm">--</div>
    <div class="date" id="date">----/--/--</div>
    <div class="date" id="hijriDate" style="color:#f6c945;font-size:clamp(14px,3.3vw,20px);margin-top:2px">-- هجري</div>
  </div>

  <div class="prayers" id="prayers">
    <div class="card" id="card-Fajr"><div class="name">الفجر</div><div class="time" id="time-Fajr">--:--</div><div class="period" id="period-Fajr">--</div><div class="iqama">الإقامة: <span id="iq-Fajr">28</span> د</div><div class="iqControls"><button class="iqBtn" data-k="Fajr" data-d="-1">−</button><span class="iqVal" id="ctl-Fajr">28</span><button class="iqBtn" data-k="Fajr" data-d="1">+</button></div></div>
    <div class="card" id="card-Sunrise"><div class="name">الشروق</div><div class="time" id="time-Sunrise">--:--</div><div class="period" id="period-Sunrise">--</div><div class="iqama">—</div><div class="noIqama"></div></div>
    <div class="card" id="card-Dhuhr"><div class="name">الظهر</div><div class="time" id="time-Dhuhr">--:--</div><div class="period" id="period-Dhuhr">--</div><div class="iqama">الإقامة: <span id="iq-Dhuhr">20</span> د</div><div class="iqControls"><button class="iqBtn" data-k="Dhuhr" data-d="-1">−</button><span class="iqVal" id="ctl-Dhuhr">20</span><button class="iqBtn" data-k="Dhuhr" data-d="1">+</button></div></div>
    <div class="card" id="card-Asr"><div class="name">العصر</div><div class="time" id="time-Asr">--:--</div><div class="period" id="period-Asr">--</div><div class="iqama">الإقامة: <span id="iq-Asr">20</span> د</div><div class="iqControls"><button class="iqBtn" data-k="Asr" data-d="-1">−</button><span class="iqVal" id="ctl-Asr">20</span><button class="iqBtn" data-k="Asr" data-d="1">+</button></div></div>
    <div class="card" id="card-Maghrib"><div class="name">المغرب</div><div class="time" id="time-Maghrib">--:--</div><div class="period" id="period-Maghrib">--</div><div class="iqama">الإقامة: <span id="iq-Maghrib">12</span> د</div><div class="iqControls"><button class="iqBtn" data-k="Maghrib" data-d="-1">−</button><span class="iqVal" id="ctl-Maghrib">12</span><button class="iqBtn" data-k="Maghrib" data-d="1">+</button></div></div>
    <div class="card" id="card-Isha"><div class="name">العشاء</div><div class="time" id="time-Isha">--:--</div><div class="period" id="period-Isha">--</div><div class="iqama">الإقامة: <span id="iq-Isha">15</span> د</div><div class="iqControls"><button class="iqBtn" data-k="Isha" data-d="-1">−</button><span class="iqVal" id="ctl-Isha">15</span><button class="iqBtn" data-k="Isha" data-d="1">+</button></div></div>
  </div>

  <div class="countdowns">
    <div class="countCell"><div class="countTitle" id="iqamaCountdownTitle">متبقي على الإقامة</div><div class="countValue iqamaLeft" id="iqamaCountdown">--:--:--</div></div>
    <div class="countCell"><div class="countTitle" id="adhanCountdownTitle">متبقي على الأذان</div><div class="countValue adhanLeft" id="adhanCountdown">--:--:--</div></div>
  </div>

  <div class="toolbar">
    <button class="toolBtn" id="enableAdhan">🔊 تفعيل الأذان</button>
    <button class="toolBtn" id="editMosque" title="اسم المسجد" aria-label="اسم المسجد">✏️ اسم المسجد</button>
    <button class="toolBtn" id="notesBtn" title="ملاحظات" aria-label="ملاحظات">📝 ملاحظات</button>
    <button class="toolBtn" id="qiblaBtn" title="القبلة" aria-label="القبلة">🧭 القبلة</button>
    <button class="toolBtn" id="calendarBtn" title="التقويم">📅 التقويم</button>
    <button class="toolBtn" id="adhkarBtn" title="أذكار الصباح والمساء">🤲 الأذكار</button>
    <button class="toolBtn" id="fridayBtn" title="الجمعة وساعة الإجابة">🕌 الجمعة</button>
  </div>
  <div class="settingsBox" id="settingsBox">
    <input id="mosqueInput" type="text" placeholder="اسم المسجد">
    <input id="districtInput" type="text" placeholder="اسم الحي / الموقع">
    <button id="saveMosqueSettings">حفظ الاسم والموقع</button>
  </div>
  <div class="utilityPanel" id="notesPanel">
    <h3>📝 الملاحظات والتنبيهات</h3>
    <div class="utilityGrid">
      <input id="noteDate" type="date" aria-label="تاريخ الموعد">
      <input id="noteTime" type="time" aria-label="وقت الموعد">
      <select id="noteLead" aria-label="وقت التنبيه">
        <option value="86400">🔔 قبل الموعد بـ 24 ساعة</option>
        <option value="43200">🔔 قبل الموعد بـ 12 ساعة</option>
        <option value="3600">🔔 قبل الموعد بساعة</option>
        <option value="0">🔔 عند الموعد</option>
      </select>
      <textarea id="noteText" placeholder="اكتب الملاحظة أو الموعد هنا…"></textarea>
    </div>
    <div class="utilityActions">
      <button class="utilityAction" id="saveNote">حفظ الملاحظة والتنبيه</button>
      <button class="utilityAction secondary" id="testBell">🔔 تجربة الجرس</button>
      <button class="utilityAction secondary" id="closeNotes">إغلاق</button>
    </div>
    <div class="noteList" id="noteList"></div>
  </div>

  <div class="utilityPanel" id="calendarPanel">
    <h3>📅 التقويم</h3>
    <div class="noteItem" style="text-align:center;font-size:18px"><b id="calendarGregorian"></b><br><span id="calendarHijri" style="color:#f6c945"></span></div>
    <div class="utilityActions"><button class="utilityAction secondary" id="closeCalendar">إغلاق</button></div>
  </div>

  <div class="utilityPanel" id="adhkarPanel">
    <h3>🤲 تذكير الأذكار</h3>
    <div class="noteItem">تذكير بأذكار الصباح بعد الفجر، وأذكار المساء بعد العصر. يعمل التنبيه أثناء فتح التطبيق.</div>
    <div class="utilityActions"><button class="utilityAction" id="toggleAdhkar">تفعيل التذكير</button><button class="utilityAction secondary" id="closeAdhkar">إغلاق</button></div>
  </div>

  <div class="utilityPanel" id="fridayPanel">
    <h3>🕌 الجمعة وساعة الإجابة</h3>
    <div class="noteItem" id="fridayInfo" style="text-align:center;font-size:17px"></div>
    <div class="noteItem">ساعة الإجابة: يُرجى تحرّيها يوم الجمعة، ومن أرجى أوقاتها آخر ساعة بعد العصر إلى غروب الشمس.</div>
    <div class="utilityActions"><button class="utilityAction secondary" id="closeFriday">إغلاق</button></div>
  </div>

  <div class="utilityPanel" id="qiblaPanel">
    <h3>🧭 اتجاه القبلة</h3>
    <div class="qiblaWrap">
      <div class="qiblaCompass" aria-label="بوصلة القبلة">
        <div class="qiblaArrow" id="qiblaArrow"></div>
      </div>
      <div class="qiblaInfo" id="qiblaInfo">جاري حساب اتجاه القبلة…</div>
      <div class="qiblaSmall" id="qiblaSmall">اضغط «تشغيل البوصلة» إذا أردت أن يتحرك السهم مع الجهاز.</div>
      <div class="utilityActions">
        <button class="utilityAction" id="enableCompass">تشغيل البوصلة</button>
        <button class="utilityAction secondary" id="closeQibla">إغلاق</button>
      </div>
    </div>
  </div>
  <div class="status" id="status">الساعة تعمل، والمواقيت تُحسب حسب موقع الجهاز وتقويم أم القرى.</div>
</div>

<audio id="adhanNormal" preload="auto" src="https://raw.githubusercontent.com/AalianKhan/adhans/master/adhan.mp3"></audio>
<audio id="adhanFajr" preload="auto" src="https://raw.githubusercontent.com/AalianKhan/adhans/master/adhan_fajr.mp3"></audio>

<script>
const FALLBACK={lat:26.3592,lon:43.9818,label:'بريدة - حي الرحاب'};
const DEFAULT_IQAMA={Fajr:28,Dhuhr:20,Asr:20,Maghrib:12,Isha:15};
const PRAYERS=[
 {key:'Fajr',name:'الفجر'}, {key:'Sunrise',name:'الشروق'}, {key:'Dhuhr',name:'الظهر'},
 {key:'Asr',name:'العصر'}, {key:'Maghrib',name:'المغرب'}, {key:'Isha',name:'العشاء'}
];
const SALAH_KEYS=['Fajr','Dhuhr','Asr','Maghrib','Isha'];
const $=id=>document.getElementById(id);

let iqama={...DEFAULT_IQAMA};
try{const s=JSON.parse(localStorage.getItem('tuwaijriIqamaV2')||'null');if(s)iqama={...iqama,...s}}catch(e){}
let timings=null;
let timezone='Asia/Riyadh';
let coords={...FALLBACK};
let dateLoaded='';
let adhanEnabled=false;
try{adhanEnabled=localStorage.getItem('tuwaijriAdhanEnabled')==='1'}catch(e){}
let played={};
let adhkarEnabled=false; try{adhkarEnabled=localStorage.getItem('tuwaijriAdhkarEnabled')==='1'}catch(e){}
let adhkarPlayed={};
let mosqueSettings={name:'اسم المسجد',district:''};
try{const ms=JSON.parse(localStorage.getItem('mosqueDisplaySettingsGeneralV1')||'null');if(ms)mosqueSettings={...mosqueSettings,...ms}}catch(e){}
function renderMosqueSettings(){
  if($('mosqueName')) $('mosqueName').textContent=mosqueSettings.name||'اسم المسجد';
  if($('locationText')){
    const loc=(mosqueSettings.district||coords?.label||'جاري تحديد الموقع…');
    $('locationText').textContent='📍 '+loc;
  }
  if($('mosqueInput')) $('mosqueInput').value=(mosqueSettings.name==='اسم المسجد'?'':mosqueSettings.name)||'';
  if($('districtInput')) $('districtInput').value=mosqueSettings.district||'';
}

function localParts(now=new Date()){
 const y=now.getFullYear(),mo=now.getMonth()+1,d=now.getDate(),h=now.getHours(),m=now.getMinutes(),s=now.getSeconds();
 return {year:String(y),month:String(mo).padStart(2,'0'),day:String(d).padStart(2,'0'),hour:String(h).padStart(2,'0'),minute:String(m).padStart(2,'0'),second:String(s).padStart(2,'0')};
}
function zonedParts(now=new Date()){
 try{
  const out={};
  new Intl.DateTimeFormat('en-GB',{timeZone:timezone,year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',second:'2-digit',hourCycle:'h23'}).formatToParts(now).forEach(p=>{if(p.type!=='literal')out[p.type]=p.value});
  if(out.year&&out.month&&out.day&&out.hour&&out.minute&&out.second)return out;
 }catch(e){}
 return localParts(now);
}
function dayKey(){const p=zonedParts();return `${p.year}-${p.month}-${p.day}`}
function cleanTime(v){const m=String(v||'').match(/(\d{1,2}):(\d{2})/);return m?`${m[1].padStart(2,'0')}:${m[2]}`:'00:00'}
function sec(t){const [h,m]=cleanTime(t).split(':').map(Number);return h*3600+m*60}
function hms(n){n=Math.max(0,Math.floor(n));return `${String(Math.floor(n/3600)).padStart(2,'0')}:${String(Math.floor((n%3600)/60)).padStart(2,'0')}:${String(n%60).padStart(2,'0')}`}

/* الساعة مستقلة تمامًا عن الموقع والإنترنت */
function updateClock(){
  const now=new Date();
  let h=now.getHours();
  const ap=h>=12?'PM':'AM';
  h=h%12||12;
  const clockEl=document.getElementById('clock');
  const ampmEl=document.getElementById('ampm');
  const dateEl=document.getElementById('date');
  if(clockEl) clockEl.textContent=String(h).padStart(2,'0')+':'+String(now.getMinutes()).padStart(2,'0')+':'+String(now.getSeconds()).padStart(2,'0');
  if(ampmEl) ampmEl.textContent=ap;
  if(dateEl) dateEl.textContent=now.getFullYear()+'/'+String(now.getMonth()+1).padStart(2,'0')+'/'+String(now.getDate()).padStart(2,'0');
  const hijriEl=document.getElementById('hijriDate');
  if(hijriEl){try{hijriEl.textContent=new Intl.DateTimeFormat('ar-SA-u-ca-islamic-umalqura',{day:'numeric',month:'long',year:'numeric'}).format(now)}catch(e){hijriEl.textContent=''}}
}

function renderIqama(){SALAH_KEYS.forEach(k=>{if($('iq-'+k))$('iq-'+k).textContent=iqama[k];if($('ctl-'+k))$('ctl-'+k).textContent=iqama[k]})}
function saveIqama(){try{localStorage.setItem('tuwaijriIqamaV2',JSON.stringify(iqama))}catch(e){}renderIqama()}
function setTimeCard(k,t){let [h,m]=cleanTime(t).split(':').map(Number),ap=h>=12?'PM':'AM',hh=h%12||12;$('time-'+k).textContent=`${String(hh).padStart(2,'0')}:${String(m).padStart(2,'0')}`;$('period-'+k).textContent=ap}
function renderTimes(){if(!timings)return;PRAYERS.forEach(p=>setTimeCard(p.key,timings[p.key]))}
function updateAdhanButton(){$('enableAdhan').classList.toggle('on',adhanEnabled);$('enableAdhan').textContent=adhanEnabled?'🔊 الأذان مفعّل':'🔇 تفعيل الأذان'}

/* ===== حساب أم القرى محليًا من موقع الجوال ===== */
function dtr(d){return d*Math.PI/180}
function rtd(r){return r*180/Math.PI}
function dsin(d){return Math.sin(dtr(d))}
function dcos(d){return Math.cos(dtr(d))}
function dtan(d){return Math.tan(dtr(d))}
function darcsin(x){return rtd(Math.asin(x))}
function darccos(x){return rtd(Math.acos(Math.max(-1,Math.min(1,x))))}
function darctan2(y,x){return rtd(Math.atan2(y,x))}
function darccot(x){return rtd(Math.atan2(1,x))}
function fixAngle(a){return a-360*Math.floor(a/360)}
function fixHour(a){return a-24*Math.floor(a/24)}

function julianDate(y,m,d){
  if(m<=2){y-=1;m+=12}
  const A=Math.floor(y/100),B=2-A+Math.floor(A/4);
  return Math.floor(365.25*(y+4716))+Math.floor(30.6001*(m+1))+d+B-1524.5;
}
function sunPosition(jd){
  const D=jd-2451545.0;
  const g=fixAngle(357.529+0.98560028*D);
  const q=fixAngle(280.459+0.98564736*D);
  const L=fixAngle(q+1.915*dsin(g)+0.020*dsin(2*g));
  const e=23.439-0.00000036*D;
  let RA=darctan2(dcos(e)*dsin(L),dcos(L))/15;
  RA=fixHour(RA);
  return {decl:darcsin(dsin(e)*dsin(L)),eqt:q/15-RA};
}
function midDay(jd,time){
  const eq=sunPosition(jd+time).eqt;
  return fixHour(12-eq);
}
function sunAngleTime(jd,angle,lat,time,direction){
  const decl=sunPosition(jd+time).decl;
  const noon=midDay(jd,time);
  const v=(-dsin(angle)-dsin(decl)*dsin(lat))/(dcos(decl)*dcos(lat));
  const t=darccos(v)/15;
  return noon+(direction==='ccw'?-t:t);
}
function asrTime(jd,lat,time){
  const decl=sunPosition(jd+time).decl;
  const angle=-darccot(1+dtan(Math.abs(lat-decl))); // مذهب الجمهور
  return sunAngleTime(jd,angle,lat,time,'cw');
}
function isRamadanUmmAlQura(date=new Date()){
  try{
    const parts=new Intl.DateTimeFormat('en-u-ca-islamic-umalqura',{
      timeZone:timezone,month:'numeric'
    }).formatToParts(date);
    const mo=Number((parts.find(x=>x.type==='month')||{}).value);
    return mo===9;
  }catch(e){return false}
}
function decimalToTime(x){
  x=fixHour(x);
  let total=Math.round(x*60);
  total=(total%(24*60)+(24*60))%(24*60);
  const h=Math.floor(total/60),m=total%60;
  return `${String(h).padStart(2,'0')}:${String(m).padStart(2,'0')}`;
}
function calculateUmmAlQura(lat,lon,date=new Date()){
  const p=zonedParts(date);
  const y=Number(p.year),mo=Number(p.month),d=Number(p.day);

  // السعودية كلها UTC+3. خارجها نستخدم منطقة وقت الجهاز.
  const inSaudi=(lat>=16 && lat<=33.5 && lon>=34 && lon<=56.5);
  const tz=inSaudi?3:(-date.getTimezoneOffset()/60);

  let jd=julianDate(y,mo,d)-lon/(15*24);
  const guess={Fajr:5,Sunrise:6,Dhuhr:12,Asr:13,Maghrib:18};
  const t={}; Object.keys(guess).forEach(k=>t[k]=guess[k]/24);

  let raw={};
  raw.Fajr=sunAngleTime(jd,18.5,lat,t.Fajr,'ccw');       // أم القرى: 18.5°
  raw.Sunrise=sunAngleTime(jd,0.833,lat,t.Sunrise,'ccw');
  raw.Dhuhr=midDay(jd,t.Dhuhr);
  raw.Asr=asrTime(jd,lat,t.Asr);
  raw.Maghrib=sunAngleTime(jd,0.833,lat,t.Maghrib,'cw');

  Object.keys(raw).forEach(k=>raw[k]+=tz-lon/15);

  // مواقيت أم القرى مباشرة بدون أي زيادة أو نقص يدوي على الدقائق.

  // أم القرى: العشاء بعد المغرب بـ90 دقيقة، و120 دقيقة في رمضان.
  raw.Isha=raw.Maghrib+(isRamadanUmmAlQura(date)?2:1.5);

  return {
    Fajr:decimalToTime(raw.Fajr),
    Sunrise:decimalToTime(raw.Sunrise),
    Dhuhr:decimalToTime(raw.Dhuhr),
    Asr:decimalToTime(raw.Asr),
    Maghrib:decimalToTime(raw.Maghrib),
    Isha:decimalToTime(raw.Isha)
  };
}

async function loadPrayerTimes(lat,lon,label){
  const st=$('status');
  try{
    coords={lat:Number(lat),lon:Number(lon),label:label||'حسب موقع الجهاز الحالي'};
    timezone='Asia/Riyadh';
    timings=calculateUmmAlQura(coords.lat,coords.lon,new Date());
    dateLoaded=dayKey();
    renderTimes();renderMosqueSettings();updateQiblaFromCoords();
    st.textContent='المواقيت محسوبة حسب موقع الجوال • تقويم أم القرى';
    try{localStorage.setItem('tuwaijriPrayerCacheUQ1',JSON.stringify({day:dateLoaded,timings,timezone,coords}))}catch(e){}
  }catch(e){
    try{
      const c=JSON.parse(localStorage.getItem('tuwaijriPrayerCacheUQ1')||'null');
      if(c&&c.timings){
        timings=c.timings;timezone=c.timezone||'Asia/Riyadh';coords=c.coords||coords;dateLoaded=c.day||'';
        renderTimes();renderMosqueSettings();
        st.textContent='تم استخدام آخر مواقيت أم القرى محفوظة مؤقتًا';
        return;
      }
    }catch(_){}
    st.textContent='تعذر حساب المواقيت مؤقتًا؛ الساعة نفسها مستمرة في العمل.';
  }
}

function locate(){
 $('status').textContent='جاري تحديد موقع الجهاز…';
 if(!navigator.geolocation){loadPrayerTimes(FALLBACK.lat,FALLBACK.lon,FALLBACK.label);return}
 navigator.geolocation.getCurrentPosition(
  p=>loadPrayerTimes(p.coords.latitude,p.coords.longitude,'حسب موقع الجهاز الحالي'),
  ()=>loadPrayerTimes(FALLBACK.lat,FALLBACK.lon,FALLBACK.label+' (موقع احتياطي)'),
  {enableHighAccuracy:true,timeout:10000,maximumAge:20*60*1000}
 );
}

async function unlockAdhan(){
 const a=$('adhanNormal');
 try{a.volume=0;await a.play();a.pause();a.currentTime=0;a.volume=1;adhanEnabled=true;try{localStorage.setItem('tuwaijriAdhanEnabled','1')}catch(e){}updateAdhanButton();$('status').textContent='تم تفعيل الأذان. اترك الصفحة مفتوحة وقت الصلاة.'}
 catch(e){adhanEnabled=false;try{localStorage.setItem('tuwaijriAdhanEnabled','0')}catch(_){}updateAdhanButton();$('status').textContent='تعذر تفعيل الصوت؛ اضغط الزر مرة أخرى وتأكد أن الجهاز غير صامت.'}
}
function playAdhan(key){
 if(!adhanEnabled)return;
 const a=$(key==='Fajr'?'adhanFajr':'adhanNormal');
 try{a.currentTime=0;a.volume=1;const q=a.play();if(q&&q.catch)q.catch(()=>{$('status').textContent='منع المتصفح تشغيل الأذان؛ اضغط «تفعيل الأذان» مرة واحدة.'})}catch(e){}
}

function updatePrayerState(){
 try{
  if(!timings)return;
  if(dateLoaded!==dayKey()){loadPrayerTimes(coords.lat,coords.lon,coords.label);return}
  const p=zonedParts(),h=Number(p.hour),m=Number(p.minute),s=Number(p.second),nowSec=h*3600+m*60+s;
  const salah=SALAH_KEYS.map(k=>({key:k,t:sec(timings[k])}));
  const events=[
   {key:'Fajr',t:sec(timings.Fajr)},
   {key:'Sunrise',t:sec(timings.Sunrise)},
   {key:'Dhuhr',t:sec(timings.Dhuhr)},
   {key:'Asr',t:sec(timings.Asr)},
   {key:'Maghrib',t:sec(timings.Maghrib)},
   {key:'Isha',t:sec(timings.Isha)}
  ];
  let next=events.find(x=>nowSec<x.t),adhanRemain;
  if(next){adhanRemain=next.t-nowSec}else{next={key:'Fajr',t:sec(timings.Fajr)+86400};adhanRemain=next.t-nowSec}
  $('adhanCountdown').textContent=hms(adhanRemain);
  if($('adhanCountdownTitle')) $('adhanCountdownTitle').textContent=next.key==='Sunrise'?'متبقي على الشروق':'متبقي على الأذان';
  let activeKey=next.key,iqText='--:--:--',iqBlink=false;
  let iqTitle='متبقي على الإقامة';

  // بعد دخول وقت الشروق يبقى الشروق مضاءً 15 دقيقة،
  // ويظهر عدٌّ تنازلي خاص لصلاة الشروق في خانة الإقامة.
  const sunriseSec=sec(timings.Sunrise);
  const sunriseEnd=sunriseSec+15*60;
  if(nowSec>=sunriseSec && nowSec<sunriseEnd){
   activeKey='Sunrise';
   iqTitle='متبقي على صلاة الشروق';
   iqText=hms(sunriseEnd-nowSec);
   iqBlink=(sunriseEnd-nowSec)<=60;
  }else{
   for(let i=salah.length-1;i>=0;i--){
    const x=salah[i],iq=x.t+(iqama[x.key]||0)*60,hold=iq+15*60;
    if(nowSec>=x.t&&nowSec<iq){iqText=hms(iq-nowSec);activeKey=x.key;iqBlink=(iq-nowSec)<=60;break}
    if(nowSec>=iq&&nowSec<hold){iqText='تمت الإقامة';activeKey=x.key;break}
   }
  }
  if($('iqamaCountdownTitle')) $('iqamaCountdownTitle').textContent=iqTitle;
  $('iqamaCountdown').textContent=iqText;$('iqamaCountdown').classList.toggle('blink',iqBlink);
   const iqCell=$('iqamaCountdown').closest('.countCell');
   if(iqCell)iqCell.classList.toggle('iqamaRunning',iqText!=='--:--:--' && iqText!=='تمت الإقامة');
  document.querySelectorAll('.card').forEach(c=>c.classList.remove('active'));
  const ac=$('card-'+activeKey);if(ac)ac.classList.add('active');
  const dk=dayKey();
  SALAH_KEYS.forEach(k=>{const diff=nowSec-sec(timings[k]);const mark=dk+'-'+k;if(diff>=0&&diff<6&&!played[mark]){played[mark]=1;playAdhan(k)}});
 }catch(e){
  const st=$('status');if(st)st.textContent='الساعة تعمل، لكن حدث خطأ مؤقت في تحديث مواقيت الصلاة.';
 }
}


/* ===== الملاحظات والتنبيهات ===== */
let notes=[];
try{notes=JSON.parse(localStorage.getItem('tuwaijriNotesV1')||'[]')||[]}catch(e){notes=[]}

function bellSound(){
  try{
    const C=window.AudioContext||window.webkitAudioContext;
    const ctx=new C();
    const o=ctx.createOscillator(),g=ctx.createGain();
    o.type='sine';o.frequency.value=880;g.gain.value=.0001;
    o.connect(g);g.connect(ctx.destination);
    const t=ctx.currentTime;
    g.gain.exponentialRampToValueAtTime(.35,t+.02);
    g.gain.exponentialRampToValueAtTime(.0001,t+.9);
    o.start(t);o.stop(t+1);
    setTimeout(()=>{try{ctx.close()}catch(e){}},1200);
  }catch(e){}
}
function esc(s){return String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}
function renderNotes(){
  const box=$('noteList'); if(!box)return;
  if(!notes.length){box.innerHTML='<div class="noteItem" style="text-align:center;color:#cfd7ca">لا توجد ملاحظات محفوظة.</div>';return}
  const sorted=[...notes].sort((a,b)=>a.when-b.when);
  box.innerHTML=sorted.map(n=>{
    const d=new Date(n.when);
    const when=d.toLocaleString('ar-SA',{year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit'});
    const lead=n.lead===86400?'قبل 24 ساعة':n.lead===43200?'قبل 12 ساعة':n.lead===3600?'قبل ساعة':'عند الموعد';
    return `<div class="noteItem"><div class="noteText">${esc(n.text)}</div><div class="noteMeta">${when} • التنبيه ${lead}</div><div class="noteBtns"><button type="button" data-del-note="${n.id}">حذف</button></div></div>`;
  }).join('');
  box.querySelectorAll('[data-del-note]').forEach(b=>b.addEventListener('click',()=>{
    notes=notes.filter(n=>String(n.id)!==String(b.dataset.delNote));saveNotes();
  }));
}
function saveNotes(){try{localStorage.setItem('tuwaijriNotesV1',JSON.stringify(notes))}catch(e){}renderNotes()}
function addNote(){
  const textv=$('noteText').value.trim(),dv=$('noteDate').value,tv=$('noteTime').value;
  if(!textv||!dv||!tv){$('status').textContent='اكتب الملاحظة وحدد التاريخ والوقت أولًا.';return}
  const when=new Date(`${dv}T${tv}:00`).getTime();
  if(!Number.isFinite(when)){ $('status').textContent='التاريخ أو الوقت غير صحيح.'; return }
  notes.push({id:Date.now(),text:textv,when,lead:Number($('noteLead').value)||0,fired:false});
  saveNotes();$('noteText').value='';$('status').textContent='تم حفظ الملاحظة والتنبيه.';
}
function checkNotes(){
  const now=Date.now();let changed=false;
  for(const n of notes){
    const alarm=n.when-(n.lead||0)*1000;
    if(!n.fired && now>=alarm && now<alarm+65000){
      n.fired=true;changed=true;bellSound();
      alert('🔔 تذكير\n\n'+n.text);
    }
  }
  if(changed)saveNotes();
}
function setDefaultNoteDate(){
  const d=new Date(Date.now()+24*3600*1000);
  if(!$('noteDate').value)$('noteDate').value=d.toISOString().slice(0,10);
  if(!$('noteTime').value)$('noteTime').value='09:00';
}

/* ===== التقويم والأذكار والجمعة ===== */
function hijriText(d=new Date()){try{return new Intl.DateTimeFormat('ar-SA-u-ca-islamic-umalqura',{weekday:'long',day:'numeric',month:'long',year:'numeric'}).format(d)}catch(e){return ''}}
function renderCalendar(){const d=new Date();$('calendarGregorian').textContent=new Intl.DateTimeFormat('ar-SA',{weekday:'long',day:'numeric',month:'long',year:'numeric'}).format(d);$('calendarHijri').textContent=hijriText(d)}
function renderAdhkarButton(){$('toggleAdhkar').textContent=adhkarEnabled?'إيقاف التذكير':'تفعيل التذكير';$('toggleAdhkar').classList.toggle('on',adhkarEnabled)}
function checkAdhkar(){if(!adhkarEnabled||!timings)return;const p=zonedParts(),now=Number(p.hour)*60+Number(p.minute),today=dayKey();[['morning','Fajr','أذكار الصباح'],['evening','Asr','أذكار المساء']].forEach(([id,k,msg])=>{const [h,m]=cleanTime(timings[k]).split(':').map(Number),target=h*60+m+10,key=today+'-'+id;if(now>=target&&now<target+2&&!adhkarPlayed[key]){adhkarPlayed[key]=1;bellSound();$('status').textContent='🤲 تذكير: '+msg}})}
function renderFriday(){const d=new Date(),days=(5-d.getDay()+7)%7,next=new Date(d);next.setDate(d.getDate()+days);const label=days===0?'اليوم الجمعة':'الجمعة القادمة';let txt=label+': '+new Intl.DateTimeFormat('ar-SA',{day:'numeric',month:'long',year:'numeric'}).format(next);if(days===0&&timings){txt+=' — المغرب '+format12(timings.Maghrib).text+' '+format12(timings.Maghrib).period+'، ويُرجى تحرّي ساعة الإجابة قبل المغرب.'}$('fridayInfo').textContent=txt}
function closeUtilityPanels(){['notesPanel','qiblaPanel','calendarPanel','adhkarPanel','fridayPanel'].forEach(id=>{if($(id))$(id).classList.remove('show')});$('settingsBox').classList.remove('show')}

/* ===== اتجاه القبلة ===== */
const KAABA={lat:21.4225,lon:39.8262};
let qiblaBearing=0,deviceHeading=null;
function toRad(x){return x*Math.PI/180}
function toDeg(x){return x*180/Math.PI}
function calcQibla(lat,lon){
  const p1=toRad(lat),p2=toRad(KAABA.lat),dl=toRad(KAABA.lon-lon);
  const y=Math.sin(dl)*Math.cos(p2);
  const x=Math.cos(p1)*Math.sin(p2)-Math.sin(p1)*Math.cos(p2)*Math.cos(dl);
  return (toDeg(Math.atan2(y,x))+360)%360;
}
function renderQibla(){
  const arrow=$('qiblaArrow');
  if(!arrow)return;
  const rot=deviceHeading==null?qiblaBearing:(qiblaBearing-deviceHeading+360)%360;
  arrow.style.transform=`translate(-50%,-100%) rotate(${rot}deg)`;
  $('qiblaInfo').textContent=`اتجاه القبلة: ${Math.round(qiblaBearing)}° من الشمال`;
  $('qiblaSmall').textContent=deviceHeading==null
    ?'السهم يوضح اتجاه القبلة بالنسبة للشمال. شغّل البوصلة ليصبح متوافقًا مع اتجاه الجهاز.'
    :`اتجاه الجهاز: ${Math.round(deviceHeading)}° • وجّه أعلى الهاتف مع السهم.`;
}
function updateQiblaFromCoords(){
  qiblaBearing=calcQibla(coords.lat,coords.lon);renderQibla();
}
function orientationHandler(e){
  let h=null;
  if(typeof e.webkitCompassHeading==='number') h=e.webkitCompassHeading;
  else if(typeof e.alpha==='number') h=(360-e.alpha)%360;
  if(h!=null){deviceHeading=h;renderQibla()}
}
async function enableCompass(){
  try{
    if(typeof DeviceOrientationEvent!=='undefined' && typeof DeviceOrientationEvent.requestPermission==='function'){
      const p=await DeviceOrientationEvent.requestPermission();
      if(p!=='granted')throw new Error('denied');
    }
    window.removeEventListener('deviceorientation',orientationHandler,true);
    window.addEventListener('deviceorientation',orientationHandler,true);
    $('qiblaSmall').textContent='حرّك الهاتف قليلًا لمعايرة البوصلة…';
  }catch(e){
    $('qiblaSmall').textContent='تعذر تشغيل بوصلة الجهاز؛ سيبقى اتجاه القبلة ظاهرًا بالدرجات.';
  }
}

document.querySelectorAll('.iqBtn').forEach(b=>b.addEventListener('click',()=>{const k=b.dataset.k,d=Number(b.dataset.d);iqama[k]=Math.max(0,Math.min(120,(iqama[k]||0)+d));saveIqama()}));
saveIqama();
$('enableAdhan').addEventListener('click',()=>{if(adhanEnabled){adhanEnabled=false;try{localStorage.setItem('tuwaijriAdhanEnabled','0')}catch(e){}updateAdhanButton();$('status').textContent='تم إيقاف الأذان.'}else unlockAdhan()});

$('editMosque').addEventListener('click',()=>{$('settingsBox').classList.toggle('show');renderMosqueSettings()});
$('saveMosqueSettings').addEventListener('click',()=>{
  mosqueSettings.name=$('mosqueInput').value.trim()||'اسم المسجد';
  mosqueSettings.district=$('districtInput').value.trim()||'';
  try{localStorage.setItem('mosqueDisplaySettingsGeneralV1',JSON.stringify(mosqueSettings))}catch(e){}
  renderMosqueSettings();$('settingsBox').classList.remove('show');$('status').textContent='تم حفظ اسم المسجد والحي.';
});

$('notesBtn').addEventListener('click',()=>{
  $('qiblaPanel').classList.remove('show');
  $('settingsBox').classList.remove('show');
  $('notesPanel').classList.toggle('show');
  setDefaultNoteDate();renderNotes();
});
$('qiblaBtn').addEventListener('click',()=>{
  $('notesPanel').classList.remove('show');
  $('settingsBox').classList.remove('show');
  $('qiblaPanel').classList.toggle('show');
  updateQiblaFromCoords();
});
$('saveNote').addEventListener('click',addNote);
$('testBell').addEventListener('click',()=>{bellSound();$('status').textContent='تم تشغيل جرس التجربة.'});
$('closeNotes').addEventListener('click',()=>$('notesPanel').classList.remove('show'));
$('closeQibla').addEventListener('click',()=>$('qiblaPanel').classList.remove('show'));
$('enableCompass').addEventListener('click',enableCompass);
$('calendarBtn').addEventListener('click',()=>{const was=$('calendarPanel').classList.contains('show');closeUtilityPanels();if(!was){renderCalendar();$('calendarPanel').classList.add('show')}});
$('adhkarBtn').addEventListener('click',()=>{const was=$('adhkarPanel').classList.contains('show');closeUtilityPanels();if(!was){renderAdhkarButton();$('adhkarPanel').classList.add('show')}});
$('fridayBtn').addEventListener('click',()=>{const was=$('fridayPanel').classList.contains('show');closeUtilityPanels();if(!was){renderFriday();$('fridayPanel').classList.add('show')}});
$('closeCalendar').addEventListener('click',()=>$('calendarPanel').classList.remove('show'));
$('closeAdhkar').addEventListener('click',()=>$('adhkarPanel').classList.remove('show'));
$('closeFriday').addEventListener('click',()=>$('fridayPanel').classList.remove('show'));
$('toggleAdhkar').addEventListener('click',()=>{adhkarEnabled=!adhkarEnabled;try{localStorage.setItem('tuwaijriAdhkarEnabled',adhkarEnabled?'1':'0')}catch(e){}renderAdhkarButton();$('status').textContent=adhkarEnabled?'تم تفعيل تذكير أذكار الصباح والمساء.':'تم إيقاف تذكير الأذكار.'});
renderNotes();
setInterval(checkNotes,15000);
setInterval(checkAdhkar,30000);

renderMosqueSettings();

renderIqama();
updateAdhanButton();
updateClock();
setInterval(updateClock,1000);
setInterval(updatePrayerState,1000);
window.addEventListener('focus',updateClock);
window.addEventListener('pageshow',()=>{updateClock();updatePrayerState()});
document.addEventListener('visibilitychange',()=>{if(!document.hidden){updateClock();updatePrayerState()}});
locate();
setInterval(()=>loadPrayerTimes(coords.lat,coords.lon,coords.label),30*60*1000);


/* ===== تشغيل كتطبيق على الجوال ===== */
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('./sw.js').catch(()=>{});
  });
}
function isStandaloneMode(){
  return window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone === true;
}
window.addEventListener('load',()=>{
  if(isStandaloneMode()){
    const st=document.getElementById('status');
    if(st && !st.textContent.includes('المواقيت')) st.textContent='تعمل الآن كساعة مستقلة على شاشة الجوال.';
  }
});

</script>
</body>
</html>

'''

components.html(HTML, height=1650, scrolling=True)
