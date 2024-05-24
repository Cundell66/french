from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from tts import tts
from flask import render_template, Flask, redirect, request
import jinja_partials
import uuid

chat = ChatGroq(temperature=0, groq_api_key="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", model_name="llama3-70b-8192")

app = Flask(__name__)
jinja_partials.register_extensions(app)

system = "You are the worlds best anglo-french translation assistant. You translate every statement from engliah to french without additional conversation."
human = "{text}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
response = ""
sound_file = ""
unique_id = ""


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def translate():
    text = request.form.get("phrase")
    chain = prompt | chat
    response = chain.invoke({"text": text}).content
    sound_file=tts(response)
    unique_id = str(uuid.uuid4())
    return render_template("index.html", response=response, sound_file = sound_file, unique_id = unique_id)
