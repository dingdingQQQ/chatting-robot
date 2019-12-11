# 妹妹養成 Chatbot

## Setup

### Prerequisite
* Python 3
* Line

#### Install Dependency
```sh
pip3 install -r requirements.txt
```

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](https://i.imgur.com/2ygnl6u.png)

## Usage
The initial state is set to `user`.

* state:user

	* Input: "start"
	  * state:choose
	  * Reply: "妹妹不開心要怎麼辦？ 1.帶她去吃甜點(sweet) 2.帶她去遊樂園玩(play) 3.帶她去買東西(buy)"

		* Input: "sweet"
		  * state: wellbehave
		  * Reply: "養成乖巧的妹妹>w<" (回到 user state)

		* Input: "play"
		  * state: cute
		  * Reply: "養成可愛的妹妹>w<" (回到 user state)

		* Input: "buy"
		  * state: princess
		  * Reply: "妹妹在學校和別人打架，你會？ 1.去學校揍那個人(fight) 2.責怪妹妹(blame) 3.釐清事情真相(clarify)"

			* Input: "fight"
	  		  * state: princessfinish
	  		  * Reply: "養成公主病妹妹:(" (回到 user state)

			* Input: "blame"
	  		  * state: bad
	  		  * Reply: "養成脾氣不好的妹妹:(" (回到 user state)
			
			* Input: "clarify"
	  		  * state: wellbehave
	  		  * Reply: "養成乖巧的妹妹>w<" (回到 user state)