var ses = require('node-ses');  
var ses_client = ses.createClient({ key: 'AKIAIOHNP33JNUJN2CKA', secret: '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' });  

  exports.handler = (event, context, callback) => {
    // TODO implement
        
      // Give SES the details and let it construct the message for you.   
      ses_client.sendEmail({  
      to: 'aw3001@columbia.edu'  
      , from: 'weiyimingege@gmail.com'  
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




