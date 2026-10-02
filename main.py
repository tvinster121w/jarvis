from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass
    from android.runnable import run_on_ui_thread
    WebView = autoclass('android.webkit.WebView')
    WebViewClient = autoclass('android.webkit.WebViewClient')
    Activity = autoclass('org.kivy.android.PythonActivity')
    LayoutParams = autoclass('android.view.ViewGroup$LayoutParams')
    LinearLayout = autoclass('android.widget.LinearLayout')


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
        webview.getSettings().setJavaScriptEnabled(True)
        webview.getSettings().setDomStorageEnabled(True)
        webview.getSettings().setMediaPlaybackRequiresUserGesture(False)
        webview.setWebViewClient(WebViewClient())
        webview.loadUrl('https://tvinster121w.github.io/jarvis/')
        view = activity.findViewById(1)
        view.addView(
            webview,
            LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT)
        )


if __name__ == '__main__':
    JarvisApp().run()
