import { useState, useCallback } from "react";
import { Send24Filled } from "@fluentui/react-icons";
import {
  makeStyles,
  Input,
  Persona,
  shorthands,
  Divider,
  tokens,

} from "@fluentui/react-components";

import botAvatar from "../assets/logo.jpg";

import ThreeDots from "./ThreeDots";
import {useDropzone} from 'react-dropzone'

const useStyles = makeStyles({
  wrapper: {
    display: "flex",
    width: "100%",
    justifyContent: "center",
    height: "100vh",
    backgroundColor: tokens.colorNeutralBackground2
  },
  root: {
    display: "flex",
    ...shorthands.padding("20px"),
    flexDirection: "column",
    width: "50%",
    justifyContent: "center",
    backgroundColor: tokens.colorNeutralBackground1
  },
  chatBox: {
    display: "flex",
    height: "100%",
    width: "100%",
    flexDirection: "column",
    overflowY: "auto",
  },
  tools: {
    width: "100%",
  },
  messageBox: {
    width: "100%",
  },
  header: {
    height: "10%",
    width: "100%",
  },

  meMessageBubble: {
    ...shorthands.margin("10px"),
    width: "60%",
    ...shorthands.padding("10px"),
    ...shorthands.borderRadius("10px"),
    backgroundColor: "#0078d4",
    alignSelf: "flex-end",
    color: "#fff",
  },
  botMessageBubble: {
    ...shorthands.margin("10px"),
    width: "60%",
    ...shorthands.padding("10px"),
    ...shorthands.borderRadius("10px"),
    backgroundColor: "#eaeaea",
    alignSelf: "flex-start",
    color: "#000",
  },

  botLoadingMessageBubble: {
    ...shorthands.margin("10px"),
    width: "10%",
    ...shorthands.padding("10px"),
    ...shorthands.borderRadius("10px"),
    backgroundColor: "#eaeaea",
    alignSelf: "flex-start",
    color: "#000",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  },
  messageContainer: {
    display: "flex",
    flexDirection: "column",
  },
});

interface Message {
  user: string;
  text: string;
}

const url: string = "http://localhost:5000";   //Use if running via docker
//const url: string = "";  //Use if running locally

const userName = "me";

function App() {
  const classes = useStyles();
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");

  const [loading, setLoading] = useState(false);

  const scrollToBottom = () => {
    const chatBox = document.getElementById("chatBox");
    if (chatBox != null)
      chatBox.scrollTop = chatBox.scrollHeight;
  };

  const sendMessage = async (message: Message) => {
    setLoading(true);
    scrollToBottom();
    const response = await fetch(`${url}/prompt`, {
      method: "POST",
      body: JSON.stringify({ prompt: message.text }),
      headers: {
        "Content-Type": "application/json",
      },
    });

    const data = await response.json();
    setMessages((current) => [
      ...current,
      { user: "bot", text: data.response },
    ]);
    setLoading(false);
    scrollToBottom();
  };

  const onSend = () => {
    const msg = { user: userName, text: input };
    setMessages([...messages, msg]);
    sendMessage(msg);
    setInput("");
  };

  const uploadFile = async (file: File) => {
    console.log(`Uploading file ${file.name}`);
    const formData = new FormData();
    formData.append("file", file, file.name);
    setMessages((current) => [
      ...current,
      { user: "bot", text: `Processing file ${file.name}, I'll let you know when I've finished.`},
    ]);
    setLoading(true);
    scrollToBottom();
    const response = await fetch(`${url}/document`, {
      method: "POST",
      body: formData
    });

    const json = await response.json();
    setMessages((current) => [
      ...current,
      { user: "bot", text: `I've finished processing ${file.name}, you can ask me questions about it.`},
    ]);
    setLoading(false);
    scrollToBottom();
    console.log(`Json returned: ${json}`);
  };


  const onDrop = useCallback((acceptedFiles: File[]) => {
      acceptedFiles.forEach((file) => {
       uploadFile(file);
      })
    }, [])
    const {getRootProps, getInputProps} = useDropzone({onDrop})


  return (
    <>
      <div className={classes.wrapper}>
        <div className={classes.root}>

          <h1>DisCopilot</h1>
          <h3>A Disconnected Copilot</h3>
          <br />
          <Divider />
          <br />


          <div id="chatBox" className={classes.chatBox} {...getRootProps()}>
          <input {...getInputProps()} />
            <div className={classes.header}>
              <Persona
                name="Disconnected CoPilot Bot"
                secondaryText="Almost Human"
                avatar={{
                  image: {
                    src: botAvatar,
                    width: '100px'
                  },
                }}
                presence={{
                  status: "available",
                }}
              />
            </div>
            <div className={classes.messageContainer}>
              {messages.map((message) => (
                <div
                  className={
                    message.user == userName
                      ? classes.meMessageBubble
                      : classes.botMessageBubble
                  }
                >
                  {message.text}
                </div>
              ))}
              {loading && (
                <div className={classes.botLoadingMessageBubble}>
                  <ThreeDots />
                </div>
              )}
            </div>
          </div>
          <div className={classes.tools}>
            <Input
            appearance="underline"
            contentAfter={<Send24Filled />}
              onKeyPress={(k) => {
                if (k.key === "Enter") {
                  onSend();
                }
              }}
              className={classes.messageBox}
              value={input}
              onChange={(e) => { setInput(e.target.value) }}
            />
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
