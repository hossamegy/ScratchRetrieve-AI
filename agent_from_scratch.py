from langchain_google_genai import ChatGoogleGenerativeAI
import re

class SimpleAgent:
    def __init__(self, model_name, known_actions, system=''):
        self.model_name = model_name
        self.known_actions = known_actions
        self.system = system
        self.messages = []
        if self.system:
            self.messages.append({"role": "system", "content": system})
   
    def __call__(self, message):
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        return result

    def execute(self):
        llm = ChatGoogleGenerativeAI(model=self.model_name)
        return llm.invoke(self.messages).content

    def query(self, question,  max_turns=5):  
        action_re = re.compile(r'^Action: (\w+): (.*)$')
        i = 0
        next_prompt = question
        
        while i < max_turns:
            i += 1
            result = self(next_prompt)
            print(result)
            
            actions = [action_re.match(a) for a in result.split('\n') if action_re.match(a)]
            
            if actions:
                action, action_input = actions[0].groups()
                if action not in self.known_actions:
                    raise Exception(f"Unknown action: {action}: {action_input}")
                print(f" -- running {action} {action_input}")
                observation = self.known_actions[action](action_input)
                print("Observation:", observation)
                next_prompt = f"Observation: {observation}"
            else:
                return "STOP"





