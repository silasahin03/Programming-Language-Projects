open

&value1 let 8.
&value2 let 16.
&value3 let 2.
&value4 let 5.

&result1 let &value1 ++ &value3.
&result2 let &value2 -- &value1.
&result3 let &value2 // &value3.
&result4 let &value1 ** &value3.

&result1 write.
&result2 write.
&result3 write.
&result4 write.

whether{5 smaller &result3 ^ &value4 not== 6} <
	&result3 write.
>.

when &value1 bigger 2 do <
	&value4 let &value4 ++ 5.
	&value1 let &value1 -- 1.
>.

6 times <
	&value3 let &value3 ** 2.
	&value3 write.
>.

whether 8 smaller 10 <
	100 write.
>.


close
