import frida
import time

device = frida.get_usb_device()
pid = device.spawn("com.android.insecurebankv2")
device.resume(pid)

time.sleep(1) # sleep 1 to avoid crash (sometime)

session=device.attach(pid)

hook_script="""
Java.perform
(
    function()
    {
        console.log("Inside the hook_script");
        cryptoClass = Java.choose('com.android.insecurebankv2.CryptoClass',
        {
            onMatch : function(instance)
            {
                console.log("Found instance: " + instance);
                console.log("Result decrypt: " + instance.aesDeccryptedstring("v/sIpihDCo2ckDRLWSUniw=="));
            },
            onComplete: function()
            {
                console.log("Search completed");
            }
        });
    }
);            
"""
script=session.create_script(hook_script)
script.load()

input('...?')
