if __name__ == "__main__":
    try:
    	while True:
    		code=raw_input()
    		comsplit=code.split('//',1)
    		print comsplit[0].replace('->','.')+code[len(comsplit[0]):]
    except EOFError:
    	pass
