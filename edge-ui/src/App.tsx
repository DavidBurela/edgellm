import { useState } from 'react'
import { Send24Filled } from "@fluentui/react-icons";
import { makeStyles, Input, Persona, shorthands, Divider } from '@fluentui/react-components';

import ThreeDots  from './ThreeDots'

const useStyles = makeStyles({
  wrapper: {
    display: 'flex',
    width: '100%',
    justifyContent: 'center',
    backgroundColor: '#f5f5f5',
    height: '100vh',
  },
  root: {
    display: 'flex',
    ...shorthands.padding('20px'),
    flexDirection: 'column',
    width: '50%',
    justifyContent: 'center',
    backgroundColor: '#fff',
  },
  chatBox: {
    display: 'flex',
    height:'100%',
    width: '100%',
    flexDirection: 'column',
  },
  tools: {
    width: '100%',
  },
  messageBox: {
    width: '100%',
  },
  header: {
    height: '10%',
    width: '100%',
  },


  meMessageBubble: {
    ...shorthands.margin('10px'),
    width: "60%",
    ...shorthands.padding('10px'),
    ...shorthands.borderRadius('10px'),
    backgroundColor: '#0078d4',
    alignSelf: 'flex-end',
color: '#fff',}
,
  botMessageBubble: {
    ...shorthands.margin('10px'),
    width: "60%",
    ...shorthands.padding('10px'),
    ...shorthands.borderRadius('10px'),
    backgroundColor: '#eaeaea',
    alignSelf: 'flex-start',
    color: '#000',
  },

  botLoadingMessageBubble: {
    ...shorthands.margin('10px'),
    width: "10%",
    ...shorthands.padding('10px'),
    ...shorthands.borderRadius('10px'),
    backgroundColor: '#eaeaea',
    alignSelf: 'flex-start',
    color: '#000',
    display:'flex',
    justifyContent: 'center',
    alignItems: 'center'
  },
  messageContainer: {
    display: 'flex',
    flexDirection: 'column',
  }
});


interface Message {
  user: string
  text: string
}

const url: string = "http://127.0.0.1:5000"

const userName = "me"

function App() {
  const classes = useStyles();
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')

  const [loading, setLoading] = useState(true)

  const sendMessage = async (message: Message) => {
    setLoading(true)
    const response = await fetch(`${url}`, {
      method: 'POST',
      body: JSON.stringify({prompt: message.text}),
      headers: {
        'Content-Type': 'application/json'
      },
    })
     
    const data = await response.json()
    setMessages(current => [...current, { user: 'bot', text: data.response}])
    setLoading(false)
  }


  const onSend = () => {
    const msg = { user: userName, text: input }
    setMessages([...messages, msg])
    sendMessage(msg)
    setInput('')
  }

  return (
    <>
    <div className={classes.wrapper}>
      <div className={classes.root}>
      <h1>Mission CoPilot</h1>
      <br/>
      <Divider/>
      <br/>
      <div className={classes.chatBox}>
        <div className={classes.header}>
          <Persona 
            name="Mission CoPilot Bot"
            secondaryText="Almost Human"
            avatar={{ 
              image: {
                src:'./assets/avatar.jpg' 
              }
            }}
            presence={{
              status: 'available',
            }}
            />
        </div>
        <div className={classes.messageContainer}>
        {messages.map((message) => (
          <div className={message.user == userName ? classes.meMessageBubble : classes.botMessageBubble }>{message.text}</div>
        ))}
        {loading && <div className={classes.botLoadingMessageBubble}  >
          <ThreeDots/>
        </div>}
        </div>
      
      </div>
      <div className={classes.tools}>
      <Input contentAfter={<Send24Filled/>} onKeyPress={(k)=> {
        if (k.key === 'Enter') {
          onSend()
        }
      }} className={classes.messageBox} value={input} onChange={(e) => setInput(e.target.value)} />
        </div>
      </div>
     
      </div>
    </>
  )
}

export default App
