var i=2; var num=7883;
while( i < num) {
	if(num % i === 0){
		console.log("false");
		break;
	}
	i++;
}
if (i===num){
	console.log("true");
}
