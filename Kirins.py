text = "La, la-la-la, la-la La-la-la, la-la-la The Kirin used to speak and sing We weren't always quiet We told stories and funny jokes My stand-up was a riot But then one day, a fight broke out And hurtful words were said Flaring tempers were inflamed Destruction quickly spread And flaming bred from head to head It even burnt our... bread Sorry, I forgot how much I love rhyming. Where was I? Oh, right! My happy village lay in ruins Relationships got worse Spoiler alert: we quickly learned That words could be a curse No more talking, yelled our leader The last thing said aloud into the Stream of Silence We stepped as a crowd The water cooled emotions And peace was soon restored But with no way to speak my thoughts I got super... bored Seriously, there's only so long that Sudoku can keep you entertained! 'Cause rainbows won't light up the sky Unless you let it rain And shiny apples sometimes come with worms No, you can't give up your laughter 'Cause you're scared of a little pain It's a lesson that the Kirin never learned I was stuck in silent prison With the voices in my head 'Til I tripped over my salvation In a helpful flowerbed I found a cure to clear my pipes And I became quite chatty With years and years of stored-up words I drove my village batty They didn't like my jokes and songs And daily dose of news The plays I wrote, the speeches spoke Variety revues Or the story about the Kirin who hid below an opera stage And fell in love with this opera singer, and he wore a freaky half-mask thing, and he played the organ a lot and got all broody 'cause the singer was in love with another dude, so he took her away on this underground gondola. I mean, who doesn't love musical theater?! he village leader made it clear I had to make my choice I could stay and live with them Or I could keep my voice So I came here, but left the couch alone They're hard to move With just the view for company Until ya heard me groove Take it away, boys! [beat] 'Cause rainbows won't light up the sky Unless you let it rain And candles just won't glow until they're burned No, you can't give up your laughter 'Cause you're scared of a little pain It's a lesson that my village never learned No matter how hard I schooled them Fear of hurt is still what ruled them Sometimes you gotta let it raaaaaaaain! Yeah, sometimes you've gotta let it rain'"
pattern = 'Kirin'
pattern_sum, work_sum, a = (0,0,0)
result, a = ([], []) 
for i in range (0,len(pattern)):
    pattern_sum += ord(pattern[i])
for i in range (0,len(pattern)):
    work_sum += ord(text[i])
print (work_sum, pattern_sum)
for i in range (len(text)-len(pattern)):
    if work_sum == pattern_sum: result.append(i)
    work_sum += (ord(text[i+len(pattern)]) - ord(text[i]))
for i in result:
    if text[i:i+len(pattern)] == pattern: a.append(i+1)
result = a
print (result)
for i in result: print (text[i-1:i+len(pattern)])
