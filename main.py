from llm import get_llm
from langchain_core.messages import AIMessage , HumanMessage , SystemMessage
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate 
class Response(BaseModel):
    """an answer to the user question alog with justification """
    answer : str = Field(... , description="the answer to the user question")
    justification : str = Field(... , description="the justification for the answer")

def talk():
    system_mess = SystemMessage("you are halpful assistant that responds to question" \
    "with three exclamation marks")
    model = get_llm(temperature=0.6 , max_tokens=512)

    while True:
        structured_output = model.with_structured_output(Response)
        user = input("ask question ")
        if user.lower() == "exit":
            break
        response = structured_output.invoke([system_mess, HumanMessage(user)])
        print(response)
def token_stream():
    system_mess = SystemMessage(
        "you are a helpful assistant that responds to questions"
    )
    model = get_llm(temperature=0.6, max_tokens=512)

    while True:
        user = input("ask question ")
        if user.lower() == "exit":
            break

        for token in model.stream([
            system_mess,
            HumanMessage(user),
        ]):
            print(token.content, end="", flush=True)

        print()

def using_LCEL():
    prompt = ChatPromptTemplate.from_messages([
        {
            "role": "system" , "content" : "you are a helpful assistant that responds to questions",

        },
        {
            "role": "human" , "content" : "{question}"
        }
    ])

    model = get_llm(temperature=0.6, max_tokens=512)
    chain = prompt | model
    while True:
        user  = input("ask question: ")
        if user.lower() == "exit":
            break
        for token in chain.stream({"question": user}):
            print(token.content, end="", flush=True)
        print()


if __name__ == "__main__":
    #talk()
    #token_stream()
    using_LCEL()