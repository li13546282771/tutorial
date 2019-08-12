// 第一个导航栏
var pannel = document.getElementsByClassName('Show-dropdown')[0];
var lis = document.getElementsByClassName('shine orange appear');
pannel.onmouseenter = liEnter;
pannel.onmouseleave = liLeave;
for(var i=0;i<lis.length;i++){
            var li=lis[i];
			li.onmouseenter = liEnter;
			li.onmouseleave = liLeave;
			li.ind = i;}
function liEnter(e){
				console.log(e.target);
				pannel.style.height = '230px';
				// if( e.target.ind != undefined ){pannel.innerHTML = data[e.target.ind]}

			}
function liLeave(){
	pannel.style.height = '0'
}


// 第二个导航栏
var photo =document.querySelector('.img2');
var next = document.querySelector('.right-button');
var prev= document.querySelector('.left-button');

//追踪圆点
var tracking = function (){
				var newLeft=photos.style.left;
				newLeft = Number(newLeft.replace('px',''));

				var activeIndex = Math.abs(newLeft/400);
				var spans = document.querySelectorAll('.buttons>span')
				// console.log(spans)
				for (var i=0; i<spans.length;i++){
				  if(i=activeIndex){
				      spans[activeIndex].style.background = "red";
				  }else {
				      spans[i].style.background = "black";
				  }
				}
				}
// 下一张
function switchNex(e){
				var currentLeft=photo.style.marginLeft;  //'-400px'
				console.log(photo.style.marginLeft);
				currentLeft= Number(currentLeft.replace('px',''));
				console.log(currentLeft);
				var newLeft =currentLeft-1226;
				if (newLeft<=-6130){//(图片个数-1)*图片宽度
				    newLeft=0
				}
				photo.style.marginLeft =String( newLeft)+'px';
				console.log(photo.style.marginLeft);
				tracking();
				}

next.onclick = switchNex;
function switchPrev(e){
				var currentLeft=photo.style.marginLeft;
				console.log(photo.style.marginLeft);
				currentLeft= Number(currentLeft.replace('px',''));
				console.log(currentLeft);
				var newLeft =currentLeft+1226;
				if (newLeft>0){//(图片个数-1)*图片宽度
				    newLeft=-4904
				}
				photo.style.marginLeft =String( newLeft)+'px';
				console.log(photo.style.marginLeft);
				tracking();
				}

prev.onclick = switchPrev;


var auto =setInterval(function () {
	var currentLeft=photo.style.marginLeft;  //'-400px'
		console.log(photo.style.marginLeft);
		currentLeft= Number(currentLeft.replace('px',''));
		console.log(currentLeft);
		var newLeft =currentLeft-1226;
		if (newLeft<=-6130){//(图片个数-1)*图片宽度
			newLeft=0
		}
		photo.style.marginLeft =String( newLeft)+'px';
		console.log(photo.style.marginLeft);
		tracking()
			}
,3000);

photo.onmouseover =function () {
	clearInterval(auto);
	auto = null;
};
photo.onmouseout = function () {
		auto =setInterval(function () {
	var currentLeft=photo.style.marginLeft;  //'-400px'
		console.log(photo.style.marginLeft);
		currentLeft= Number(currentLeft.replace('px',''));
		console.log(currentLeft);
		var newLeft =currentLeft-1226;
		if (newLeft<=-6130){//(图片个数-1)*图片宽度
			newLeft=0
		}
		photo.style.marginLeft =String( newLeft)+'px';
		console.log(photo.style.marginLeft);
		tracking();
			}
,3000);
};








