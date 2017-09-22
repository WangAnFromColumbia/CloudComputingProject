var ses = require('node-ses');  
var ses_client = ses.createClient({ key: 'AWS_KEY', secret: 'AWS_KEY' });  

  exports.handler = (event, context, callback) => {
    // TODO implement
        
      // Give SES the details and let it construct the message for you.   
      ses_client.sendEmail({  
      to: 'Email_1'  
      , from: 'Email_2'  
      , subject: 'Coupon'  
      , message: "You got a coupon" 
      , altText: 'plain text'  
      }, function (err, data, result) {  
          if (!err) {  
      callback(null, 'OK');
        }  
          else {  
      callback(null, 'KO');

          }  
          console.log(err);  
      // ...   
      });  


};




