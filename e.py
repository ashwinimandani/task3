import smtplib

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
my_id="narutouzumakivirtualassistant@gmail.com"
pswd=*******
mail.login(my_id,pswd)
mail.sendmail("narutouzumakivirtualassistant@gmail.com", "ashwinimandani8@gmail.com","Good accuracy achieve")
mail.close()
  
