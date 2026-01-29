from langchain_community.memory import zep_cloud_memory

def get_memory():
    return zep_cloud_memory(
        memory_key="chat_history",
        return_messages=True
    )


