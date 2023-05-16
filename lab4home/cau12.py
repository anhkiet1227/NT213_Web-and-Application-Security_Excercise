# import library
import frida
import sys

# implement the java code for hooking
javaCode = """
Java.perform(function () {
    send("[-] Starting hooks java.util.Random.nextInt");
    var random = Java.use("java.util.Random");
    random.nextInt.overload("int").implementation = function (var_1) {
        return -150;
    };
});
"""

# print the message
def printGetInfor(message, data):
    print(message)

# attach the process with pid change 
# remember to change the pid
process = frida.get_usb_device().attach(2331)

# create the script with java code
script = process.create_script(javaCode)

# add the message handler to print the message
script.on("message", printGetInfor)

# start hooking
print("[*] Hooking")

# load the script
script.load()

# keep the script running to read the result
sys.stdin.read()