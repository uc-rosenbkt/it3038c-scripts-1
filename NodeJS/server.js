var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require("ip");

var server = http.createServer(function(req, res){
    if(req.url === "/"){
        fs.readFile("./public/index.html","UTF-8", function(err, body){
            res.writeHead(200, {"Contet-Type":"text/html"});
            res.end(body);
        });
    }

    else if(req.url.match("/sysinfo")){
        myHostName=os.hostname();
        freemem=(os.freemem() * 0.000001).toFixed(2);
        totalmem=(os.totalmem() * 0.000001).toFixed(2);
        cpu=os.cpus().length;
        uptime=require('os').uptime;
        days=Math.floor(uptime / (3600*24));
        hours=Math.floor(uptime % (3600*24) / 3600);
        minutes=Math.floor(uptime % 3600 / 60);
        seconds=Math.floor(uptime % 60);

        html=`
        <!DOCTYPE html>
            <html>
            <head>
            <title>Node JS Respone</title>
            </head>
            <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${days} days, ${hours} hours, ${minutes} minutes, ${seconds} seconds</p>
            <p>Total Memory: ${totalmem} MB</p>
            <p>Free Memory: ${freemem} MB</p>
            <p>Number of CPUs: ${cpu}</p>
            </body>    
            </html>
        `
        res.writeHead(200, {"Content-Type":"text/html"});
        res.end(html);
    }

    else{
        res.writeHead(404, {"Content-Type":"text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
    
});

server.listen(3000);
console.log("Server listening on port 3000");