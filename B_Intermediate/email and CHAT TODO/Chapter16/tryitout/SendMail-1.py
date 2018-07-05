from SendMail import SmartMessage
msg = SmartMessage("Me <me@example.com>", "You <you@example.com>", "Your picture", "Here's that picture I took of you.")
print str(msg)
msg.addAttachment(open("photo.jpg").read(), "photo.jpg")
print str(msg)
