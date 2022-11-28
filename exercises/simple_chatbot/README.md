## Examples using Chatter and RASA library.

Before starting please create, for each exemples, a dedicated environment and install the specific requirements packages using PyPi.

After installing the requirements and adding missing pieces of code, you can run Chatter code from the command line
```
python run_chatter.py
```

For RASA, code can be found in rasa/src folder.
Please do the following in a dedicated environment moving to the rasa/src folder :
Initialize your bot within your project directory with :
```
rasa init
```
Train the bot using :
```
rasa train
```
You can use actions in a new terminal
```
rasa run actions
```
Evaluate the bot using :
```
rasa test
```
After this you can open a new terminal and start talking to your bot :
```
rasa shell
```


