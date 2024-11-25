const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;
const client = require('twilio')(accountSid, authToken);

client.message.list({ limit: 20 })
    .then(messages => messages.forEach(m => console.log(m.sid)));

    