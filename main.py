from kivy.app import App
from kivy.uix.widget import Widget
from kivy.utils import platform

PWA_URL = 'https://tvinster121w.github.io/jarvis/'

if platform == 'android':
    from jnius import autoclass
    from android.runnable import run_on_ui_thread
    WebView = autoclass('android.webkit.WebView')
    WebViewClient = autoclass('android.webkit.WebViewClient')
    Activity = autoclass('org.kivy.android.PythonActivity')
    LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')


class JarvisWidget(Widget):
    pass


class JarvisApp(App):
    def build(self):
        self.title = 'J.A.R.V.I.S.'
        if platform == 'android':
            self.start_webview()
        return JarvisWidget()

    @run_on_ui_thread
    def start_webview(self):
        activity = Activity.mActivity
        webview = WebView(activity)
        settings = webview.getSettings()
        settings.setJavaScriptEnabled(True)
        settings.setDomStorageEnabled(True)
        settings.setMediaPlaybackRequiresUserGesture(False)
        webview.setWebViewClient(WebViewClient())
        webview.loadUrl(PWA_URL)
        activity.mRootView.addView(
            webview,
            LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT)
        )


if __name__ == '__main__':
    JarvisApp().run()
