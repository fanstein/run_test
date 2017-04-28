echo “开始执行”
::${__P(thread)}
::第一个参数脚本、第二个结果文件名+时间+并发数 、第三个结果文件目录、第四个延迟时间、第五个并发数
::python ./run.py D:/项目/自由行3/1_getBookedProductInfoForDiy.jmx getBookedProductInfoForDiy ./ 10 5 >>re.log
::python ./run.py D:/项目/html转pdf/test.jmx convert ./ 0 5
python ./run.py D:/项目/html转pdf/test.jmx convert ./ 0 30 >>re.log
python ./run.py D:/项目/html转pdf/test.jmx convert ./ 0 35 >>re.log
::python ./run.py D:/项目/html转pdf/test.jmx convert ./ 0 25 >>re.log
::python ./run.py D:/项目/html转pdf/test.jmx convert ./ 60 15
::运行之前清除当前的res目录和re.log文件
pause