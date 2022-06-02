def solution(m, musicinfos):
    answer = "(None)"
    max_time=0
    m=m.replace("A#","a").replace("B#","b").replace("C#","c").replace("D#","d").replace("E#","e").replace("F#","f").replace("G#","g")
    for i in musicinfos:
        music=list(i.split(','))
        start_h,start_m=map(int,music[0].split(':'))
        end_h,end_m=map(int,music[1].split(':'))
        time=(end_h-start_h)*60+(end_m-start_m)

        music[3]=music[3].replace("A#","a").replace("B#","b").replace("C#","c").replace("D#","d").replace("E#","e").replace("F#","f").replace("G#","g")
        temp=""
        for i in range(0,time):
            temp+=music[3][i%len(music[3])]
        if m in temp and time>max_time:
            answer=music[2]
            max_time=time

    return answer
