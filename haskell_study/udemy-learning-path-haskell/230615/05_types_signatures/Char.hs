c0::Char
c0='X'

c1::Char
c1='\0088' -- 

c2::Char
c2='\x0058' -- hex

c3::Char
c3='\o0130' -- octet

main::IO()
main=do
    putChar c0 >> putChar '\n' -- X
    putChar c1 >> putChar '\n' -- X
    putChar c2 >> putChar '\n' -- X
    putChar c3 >> putChar '\n' -- X