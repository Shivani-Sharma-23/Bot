from taipy.gui import Gui

from web_pages.ChatBot.chatbot import chatbot_ui
from web_pages.Knowledge.knowledge import knowledge_ui
from web_pages.Security.security import security_ui
from web_pages.Functions.function import function_ui
from web_pages.Flow.flow import flow_ui



pages = {
    "/":"<|navbar|>",
    "ChatBot":chatbot_ui,
    "Knowledge":knowledge_ui,
    "Security":security_ui,
    "Function":function_ui,
    "Flow":flow_ui
}

if __name__ == "__main__":

    Gui(pages=pages).run(
        title="BeAlloy",
        use_reloader=True
    )


    