# Page Title: Quantum Annealing: Expert View

<!-- Added 2026-11-22. Transcript file Q2W4V5_REV_2026-en.srt (course 2, week 4, video 5) downloaded by Albert from the eDX page. Classroom recording; Albert identifies the lecturer as Peter Shor (the transcript doesn't name him). Verbatim SRT below. The page's practice question (Q1: Quantum Annealing II) is transcribed in wiki/quizzes/week-4.md from Albert's screenshot. -->

## Transcript

0
00:00:00,000 --> 00:00:00,500


1
00:00:00,500 --> 00:00:03,210
Some students ask me about D-wave after the class,

2
00:00:03,210 --> 00:00:07,380
so I think I should say something about D-wave.

3
00:00:07,380 --> 00:00:09,220
It certainly is an interesting story,

4
00:00:09,220 --> 00:00:12,710
so maybe I'll put a timeline.

5
00:00:12,710 --> 00:00:18,360
In 1999, D-wave was founded.

6
00:00:18,360 --> 00:00:22,410
And presumably they didn't come out of nowhere.

7
00:00:22,410 --> 00:00:28,890
The founders must have been doing some work before in 1999.

8
00:00:28,890 --> 00:00:36,680
In 2000, Fahri, Goldstone, Gutmann, and Sipser

9
00:00:36,680 --> 00:00:43,120
write a paper what propose adiabatic quantum computation.

10
00:00:43,120 --> 00:00:47,960
And a couple of years later, Aharanov--

11
00:00:47,960 --> 00:00:51,690


12
00:00:51,690 --> 00:00:57,450
unfortunately, I did not look up the exact date before this.

13
00:00:57,450 --> 00:00:59,740
A couple of years later, Aharanov et. al.

14
00:00:59,740 --> 00:01:01,730
Show it's universal.

15
00:01:01,730 --> 00:01:11,850
And in 2007, D-wave announces first a 16-bit prototype

16
00:01:11,850 --> 00:01:16,260
adiabatic quantum computer.

17
00:01:16,260 --> 00:01:20,350
And there is a lot of skepticism about this.

18
00:01:20,350 --> 00:01:30,940
So Scott Aaronson goes on a tirade in his blog

19
00:01:30,940 --> 00:01:36,790
and launches a crusade against them, maybe,

20
00:01:36,790 --> 00:01:39,260
saying they couldn't possibly--

21
00:01:39,260 --> 00:01:44,770
saying the things are saying couldn't possibly be true.

22
00:01:44,770 --> 00:01:57,650
And that's-- well, there's a couple of questions here.

23
00:01:57,650 --> 00:02:00,470
When they were founded, adiabatic quantum computation

24
00:02:00,470 --> 00:02:01,190
didn't exist.

25
00:02:01,190 --> 00:02:04,040
So presumably they were founded to some other kind

26
00:02:04,040 --> 00:02:05,840
of quantum computation.

27
00:02:05,840 --> 00:02:08,630
And at some point, you decide adiabatic quantum computation

28
00:02:08,630 --> 00:02:11,090
was way to go.

29
00:02:11,090 --> 00:02:19,820
And also sometime between 2007 and today,

30
00:02:19,820 --> 00:02:24,660
I couldn't figure out when, D-wave now

31
00:02:24,660 --> 00:02:30,200
says they do quantum annealing.

32
00:02:30,200 --> 00:02:32,120
So what's the difference?

33
00:02:32,120 --> 00:02:36,250
Well, adiabatic quantum computation,

34
00:02:36,250 --> 00:02:42,610
you're in the ground state and you

35
00:02:42,610 --> 00:02:47,950
would like to operate at a temperature low enough

36
00:02:47,950 --> 00:02:50,320
to stay in ground state.

37
00:02:50,320 --> 00:02:53,990
So what is this temperature?

38
00:02:53,990 --> 00:03:03,430
We call quantum adiabatic computing ground state.

39
00:03:03,430 --> 00:03:06,050
Let's have a first excited state.

40
00:03:06,050 --> 00:03:14,680
And this is what's known as an avoided crossing, where really

41
00:03:14,680 --> 00:03:17,590
this line and this line have roughly

42
00:03:17,590 --> 00:03:20,020
the same structure of the quantum state,

43
00:03:20,020 --> 00:03:22,420
as do this line and this line.

44
00:03:22,420 --> 00:03:27,250
And you get a super position of these two structures

45
00:03:27,250 --> 00:03:28,780
right here.

46
00:03:28,780 --> 00:03:32,290
And the more these two structures differ,

47
00:03:32,290 --> 00:03:39,410
the smaller the energy gap is between them.

48
00:03:39,410 --> 00:03:42,610
So that's really an oversimplification

49
00:03:42,610 --> 00:03:54,040
and waving my hands, but it is something like that.

50
00:03:54,040 --> 00:03:54,732
Yeah?

51
00:03:54,732 --> 00:03:58,176
Can you evolve your Hamiltonian quite quickly most of the time,

52
00:03:58,176 --> 00:04:00,144
and then just slow down that evolution,

53
00:04:00,144 --> 00:04:01,320
when you're going past--

54
00:04:01,320 --> 00:04:03,164
You can, you know where the gaps are,

55
00:04:03,164 --> 00:04:05,080
or rather, if you know where these things are,

56
00:04:05,080 --> 00:04:07,540
you can evolve it quickly most of the time.

57
00:04:07,540 --> 00:04:10,080
And in fact in Grover's algorithm,

58
00:04:10,080 --> 00:04:16,720
you can get a square root speed up by adiabatic computing,

59
00:04:16,720 --> 00:04:20,130
or a square root speed up over the classical search

60
00:04:20,130 --> 00:04:22,060
by adiabatic computing.

61
00:04:22,060 --> 00:04:26,520
But the way to do that, is in Grover's algorithm,

62
00:04:26,520 --> 00:04:30,100
there is one spot where you have an avoided crossing,

63
00:04:30,100 --> 00:04:35,340
which is I think 1 over square root of n.

64
00:04:35,340 --> 00:04:38,580
Anyway, to get the speed up, you have

65
00:04:38,580 --> 00:04:41,324
to go quickly most of the time, then slow down right

66
00:04:41,324 --> 00:04:42,490
before the avoided crossing.

67
00:04:42,490 --> 00:04:44,790
And then speed up right after it.

68
00:04:44,790 --> 00:04:48,390


69
00:04:48,390 --> 00:04:51,710
So yeah.

70
00:04:51,710 --> 00:04:54,890
Of course, if you don't know where these points where they

71
00:04:54,890 --> 00:04:59,300
come close are, it's going to be hard to speed up and slow down

72
00:04:59,300 --> 00:05:07,730
your evolution to account for them.

73
00:05:07,730 --> 00:05:15,020
Anyway, the temperature means that one of your qubits

74
00:05:15,020 --> 00:05:19,787
might get excited, but if you excite this state, it's not

75
00:05:19,787 --> 00:05:21,620
going to go to this state, because the state

76
00:05:21,620 --> 00:05:23,161
and this state are structurally quite

77
00:05:23,161 --> 00:05:25,560
different with excited qubit in this state,

78
00:05:25,560 --> 00:05:27,290
and I go up to this state.

79
00:05:27,290 --> 00:05:31,980
So the temperature is bigger than the smallest gap.

80
00:05:31,980 --> 00:05:32,480
OK.

81
00:05:32,480 --> 00:05:37,400
So gaps account for energy, and energy converts to temperature

82
00:05:37,400 --> 00:05:39,900
by thermodynamics.

83
00:05:39,900 --> 00:05:49,965
So right temperature is probably going to be bigger

84
00:05:49,965 --> 00:05:52,360
than the smallest gap.

85
00:05:52,360 --> 00:06:02,630
But it is still small.

86
00:06:02,630 --> 00:06:16,300
Anyway, D-wave does not operate at a temperature small enough

87
00:06:16,300 --> 00:06:19,180
to avoid thermal excitations.

88
00:06:19,180 --> 00:06:22,270
And that's not because they don't operate at a small temp--

89
00:06:22,270 --> 00:06:24,880
they operated in extremely low temperature.

90
00:06:24,880 --> 00:06:29,710
It's just that the structure of their ships

91
00:06:29,710 --> 00:06:32,962
allows for thermal excitations, even at that temperature.

92
00:06:32,962 --> 00:06:37,230


93
00:06:37,230 --> 00:06:41,140
So people were arguing with them about whether they could really

94
00:06:41,140 --> 00:06:45,760
call this quantum adiabatic computation.

95
00:06:45,760 --> 00:06:49,430
So they decided to call it quantum annealing instead.

96
00:06:49,430 --> 00:06:50,450
So what does that mean?

97
00:06:50,450 --> 00:06:53,170
Well, if it was quantum adiabatic computation,

98
00:06:53,170 --> 00:07:01,490
there would be a proof that the quantum computer was universal,

99
00:07:01,490 --> 00:07:02,940
which means that theoretically it

100
00:07:02,940 --> 00:07:08,630
could solve any problem that any quantum computer can.

101
00:07:08,630 --> 00:07:11,450
Although there is the problem of blowing up

102
00:07:11,450 --> 00:07:15,500
the size by a polynomial factor converting from the gate model

103
00:07:15,500 --> 00:07:20,330
to the adiabatic computation model and back.

104
00:07:20,330 --> 00:07:23,830
So if it really was a quantum adiabatic computer,

105
00:07:23,830 --> 00:07:29,830
they would have a good reason to claim that it could do things

106
00:07:29,830 --> 00:07:32,430
that classical computers can't.

107
00:07:32,430 --> 00:07:35,850
Well, they have a quantum annealing computer.

108
00:07:35,850 --> 00:07:39,180
it is certainly using quantum processes

109
00:07:39,180 --> 00:07:42,220
and operating in the quantum [INAUDIBLE],,

110
00:07:42,220 --> 00:07:43,320
but is it more powerful?

111
00:07:43,320 --> 00:07:46,345


112
00:07:46,345 --> 00:07:49,275
And I want to say no theoretical results.

113
00:07:49,275 --> 00:07:52,010


114
00:07:52,010 --> 00:07:57,120
So there are chips that you can program the Hamiltonian,

115
00:07:57,120 --> 00:07:59,670
and you can program a Hamiltonian to slowly change

116
00:07:59,670 --> 00:08:03,960
from one Hamiltonian to another Hamiltonian.

117
00:08:03,960 --> 00:08:06,390
And you can put the starting Hamiltonian

118
00:08:06,390 --> 00:08:08,310
into the ground state.

119
00:08:08,310 --> 00:08:17,040
And you're operating at a temperature too large

120
00:08:17,040 --> 00:08:19,500
to not have thermal excitations.

121
00:08:19,500 --> 00:08:25,710
So presumably you could take this process

122
00:08:25,710 --> 00:08:29,430
and construct some mathematical model of it.

123
00:08:29,430 --> 00:08:32,610
Although you might have to worry about what

124
00:08:32,610 --> 00:08:37,140
the right temperature for this mathematical model is.

125
00:08:37,140 --> 00:08:39,679
And then you can ask, does this mathematical model

126
00:08:39,679 --> 00:08:41,850
let you do anything that you can't

127
00:08:41,850 --> 00:08:43,320
do on classical computers?

128
00:08:43,320 --> 00:08:45,966


129
00:08:45,966 --> 00:08:48,000
And I don't know.

130
00:08:48,000 --> 00:08:48,780
Nobody knows.

131
00:08:48,780 --> 00:08:52,590


132
00:08:52,590 --> 00:08:58,530
And the other problem is that they have experiments

133
00:08:58,530 --> 00:09:01,590
that they claim show that the computer does things better

134
00:09:01,590 --> 00:09:06,020
than classical computers, but is it

135
00:09:06,020 --> 00:09:09,090
really an exponential speed up?

136
00:09:09,090 --> 00:09:20,510
Or is it just that their computer has electrical--

137
00:09:20,510 --> 00:09:24,290
it has a Hamiltonian trying to find its ground state,

138
00:09:24,290 --> 00:09:27,140
and it does this reasonably fast.

139
00:09:27,140 --> 00:09:29,300
And maybe there's a constant factor better

140
00:09:29,300 --> 00:09:32,970
than classical computers that is letting it find the ground

141
00:09:32,970 --> 00:09:35,750
state better than classical computers can,

142
00:09:35,750 --> 00:09:40,970
because physics processes can be really fast.

143
00:09:40,970 --> 00:09:44,950
So we don't really know whether D-wave is more powerful.

144
00:09:44,950 --> 00:09:50,806
