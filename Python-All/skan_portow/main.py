import telnetlib

host = "158.75.39."
port = {
    80: "HTTP",
    443: "HTTPS",
    53: "DNS",
    853: "DoT",
    123: "NTP",
    4460: "NTS",
    25: "SMTP",
    587: "SMTP",
    465: "SMTP",
    2525: "SMTP",
    110: "POP3",
    993: "POP3",
    143: "IMAP",
    995: "IMAP",
}

with open("output2 .txt", "a+") as file:
    for k, j in port.items():
        for i in range(0, 256):
            try:
                tn = telnetlib.Telnet(host + str(i), k, timeout=4)
                file.write(
                    "Port 80 is open on" + host + str(i) + "for protocol: " + j + "\n"
                )
                tn.close()
            except ConnectionRefusedError:
                file.write(
                    "Port 80 is closed on "
                    + host
                    + str(i)
                    + " for protocol: "
                    + j
                    + "\n"
                )
            except TimeoutError:
                file.write(
                    "Connection to "
                    + host
                    + str(i)
                    + " timed out "
                    + " for port: "
                    + str(k)
                    + "\n"
                )
            except Exception as e:
                file.write("An error occurred:" + str(e) + "\n")
