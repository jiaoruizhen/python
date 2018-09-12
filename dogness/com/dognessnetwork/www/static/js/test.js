function test() {
    $.ajax({
                    type : "GET",  //提交方式
                    url : "http://localhost:8000/findAll",//路径
                    // data : {
                    //     "org.id" : "${org.id}"
                    // },//数据，这里使用的是Json格式进行传输
                    dataType : "json",
                    success : function(result) {//返回数据根据结果进行相应的处理

                        console.log(result)
                        if ( result.status==1000 ) {

                             console.log(result)
                        } else {

                        }
                    },
                    error:function (error) {
                        console.log(error)
                    }
                });
}