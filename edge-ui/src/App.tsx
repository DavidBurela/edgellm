import { useState, useCallback } from "react";
import { Send24Filled } from "@fluentui/react-icons";
import {
  makeStyles,
  Input,
  Persona,
  shorthands,
  Divider,
} from "@fluentui/react-components";

import botAvatar from "./avatar.jpg";

import ThreeDots from "./ThreeDots";
import {useDropzone} from 'react-dropzone'

const useStyles = makeStyles({
  wrapper: {
    display: "flex",
    width: "100%",
    justifyContent: "center",
    backgroundColor: "#f5f5f5",
    height: "100vh",
  },
  root: {
    display: "flex",
    ...shorthands.padding("20px"),
    flexDirection: "column",
    width: "50%",
    justifyContent: "center",
    backgroundColor: "#fff",
  },
  chatBox: {
    display: "flex",
    height: "100%",
    width: "100%",
    flexDirection: "column",
    overflowY: "scroll",
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

const url: string = "";   //Use if running via docker
//const url: string = "http://127.0.0.1:5000";  //Use if running locally

const userName = "me";

function App() {
  const classes = useStyles();
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");

  const [loading, setLoading] = useState(false);

  const sendMessage = async (message: Message) => {
    setLoading(true);
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
    setMessages([...messages, { user: "bot", text: `Processing file ${file.name}, I'll let you know when I've finished.`} ]);
    const response = await fetch(`${url}/document`, {
      method: "POST",
      body: formData
    });

    const json = await response.json(); 
    setMessages([...messages, { user: "bot", text: `I've finished processing ${file.name}, you can ask me questions about it.`} ]);

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
          <h1>DisCopilot 🕺</h1>
          <br />
          <Divider />
          <br />

        
          <div className={classes.chatBox} {...getRootProps()}>
          <input {...getInputProps()} />
            <div className={classes.header}>
              <Persona
                name="CoPilot Bot"
                secondaryText="Almost Human"
                avatar={{
                  image: {
                    src: botAvatar
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
              contentAfter={<Send24Filled />}
              onKeyPress={(k) => {
                if (k.key === "Enter") {
                  onSend();
                }
              }}
              className={classes.messageBox}
              value={input}
              onChange={(e) => setInput(e.target.value)}
            />
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
