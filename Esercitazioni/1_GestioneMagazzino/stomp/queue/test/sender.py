import sys, stomp

if __name__=="__main__":


    conn = stomp.Connection([('127.0.0.1',61613)], auto_content_length=False)
    conn.connect(wait=True)
#    for i in range(30):
    msg="prova"
    conn.send('/queue/my_test', msg)

    print('Message sent - ', msg)
    conn.send('/queue/my_test', 'exit')

    conn.disconnect()
