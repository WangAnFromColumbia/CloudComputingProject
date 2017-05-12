var AWS = require('aws-sdk');
var stripe = require("stripe")("sk_test_JCy56FAehenafOCX4DpsLILx");
var jwt = require('jsonwebtoken');

function OrderError(message) {
   this.name = "OrderError";
   this.message = message;
}
OrderError.prototype = new Error();

exports.handler = function(event, context, callback) {
    console.log("**** event *****");
    console.log(event);

    try{
        var operation = event.operation;

        switch (operation) {
            case ('read'):
                // 这里直接call order的lambda, 参数：operation:"read",emial:event.email
                getCoupons(event, callback);
                break;
            case ('delete'): // 这里必须写create ？？？？？？？？？？？？
                // 这里先call Stripe lambda, 参数：stripeToken:event.stripeToken
                deleteCoupon(event, callback);

                // 确认成功则call order 参数:event.itemID 和 event.email,否则返回
                break;
            case ('create'): {
                createRawdata(event, callback);
                break;
            }
            default:
                var err = new OrderError('405 Unrecognized operation Error');
                callback(err, null);
        }
    } catch (err){
        callback(err, null);
    }
};

function getCoupons(event, callback) {
    console.log("come into getCoupons");
    var userid = event.userid;
    console.log("userid: " + userid);
    
    AWS.config.update({
        region: "us-east-1",
    });

    var docClient = new AWS.DynamoDB.DocumentClient();
    var params = {
        TableName: "recommendations",
        FilterExpression : 'UserId = :val', 
        ExpressionAttributeValues : {':val' : userid}
    };

    docClient.scan(params, function(err, data) {
        if (err) {
            err = new OrderError("500 coupon_recommended table access Error");
            callback(err, null);
        } else{
            console.log("cone into scan result");
            result = {items : data.Items
                     };
            console.log(result);
            callback(null, result);
        }
    });
}

function createRawdata(event, callback){
    console.log("come into createOrder");

    console.log("*** userid : " + event.userid + " ***");
    console.log("*** coupon_Id : " + event.coupon_Id + " ***");

    var userid = event.userid;
    var coupon_Id = event.coupon_Id;
    var rating = event.rating;

    var docClient = new AWS.DynamoDB.DocumentClient();

    var params = {
        TableName: "user_history",
        Item: {
            "UserId": userid,
            "coupon_Id": coupon_Id,
            "rating": rating,
            "timestamp" : 00000
        }
    };

    docClient.put(params, function(err, data) {
        if (err) {
            err = new OrderError("500 Order table access Error");
            console.log("error !!!");
            callback(err, null);
        } else {
            console.log(" there is no error ");
            return null;
        }
    });

    console.log(" is there any error ????");
    
}

function deleteCoupon(event, callback){
    console.log(event);
    console.log("come into deleteCoupons");

    var userid = event.userid;
    var coupon_Id = event.coupon_Id;

    console.log("*** userid : " + userid + " ***");
    console.log("*** coupon_Id : " + coupon_Id + " ***");

    var docClient = new AWS.DynamoDB.DocumentClient();

    // var params = {
    //     TableName:table,
    //     Key:{
    //         "year":year,
    //         "title":title
    //     },
    //     ConditionExpression:"info.rating <= :val",
    //     ExpressionAttributeValues: {
    //         ":val": 5.0
    //     }
    // };

    var params = {
        TableName: "recommendations",
        Key:{
            "UserId":userid
        },
        ConditionExpression : "coupon_Id = :val", 
        ExpressionAttributeValues: {
            ":val": coupon_Id
        }
    };

    docClient.delete(params, function(err, data) {
        if (err) {
            err = new OrderError("500 Order table access Error");
            callback(err, null);
        } else {
            return null;
        }
    });    
}






