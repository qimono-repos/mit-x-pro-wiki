# Page Title: Quantum Approximate Optimization Algorithm (QAOA), Farhi

<!-- Added 2026-11-22. Transcript file Q2W4V3_REV_2026-en.srt (course 2, week 4, video 3) downloaded by Albert from the eDX page. Speaker: Eddie Farhi (he names his collaborators Sam Gutmann and Jeffrey Goldstone). Missing from week5.md. The eDX page title and any Learn prose are not captured; the title above is descriptive. Verbatim SRT below. -->

## Transcript

0
00:00:00,000 --> 00:00:00,499


1
00:00:00,499 --> 00:00:04,300
We've already established I think throughout this class,

2
00:00:04,300 --> 00:00:09,280
and most of you know that optimization is a key problem

3
00:00:09,280 --> 00:00:11,930
in all of computer science.

4
00:00:11,930 --> 00:00:14,140
Now let's get a little bit more specific

5
00:00:14,140 --> 00:00:16,900
and think about what optimization means in terms

6
00:00:16,900 --> 00:00:19,240
of combinatorial search.

7
00:00:19,240 --> 00:00:23,920
There we have a problem defined on bit strings.

8
00:00:23,920 --> 00:00:28,450
And we have clauses or constraints, which

9
00:00:28,450 --> 00:00:31,300
look at subsets of the bits.

10
00:00:31,300 --> 00:00:33,940
And for certain assignments of the bits,

11
00:00:33,940 --> 00:00:36,430
those clauses are satisfied.

12
00:00:36,430 --> 00:00:38,110
And for others they are not.

13
00:00:38,110 --> 00:00:41,530
What we want to do in combinatorial optimization,

14
00:00:41,530 --> 00:00:46,090
is find a string that can satisfy

15
00:00:46,090 --> 00:00:48,490
as many clauses as possible.

16
00:00:48,490 --> 00:00:51,310
Often you can't satisfy all the clauses.

17
00:00:51,310 --> 00:00:56,200
Because the clauses have intrinsic contradictions,

18
00:00:56,200 --> 00:00:59,680
so that assignments for one clause that satisfy it,

19
00:00:59,680 --> 00:01:03,080
force other clauses to not be satisfied.

20
00:01:03,080 --> 00:01:05,440
So the question then becomes, what

21
00:01:05,440 --> 00:01:09,540
is the string that satisfies, let's say, as most clauses

22
00:01:09,540 --> 00:01:10,520
as possible?

23
00:01:10,520 --> 00:01:11,860
Now that's very ambitious.

24
00:01:11,860 --> 00:01:15,370
Because satisfying the most clauses as possible

25
00:01:15,370 --> 00:01:17,140
that's NP hard.

26
00:01:17,140 --> 00:01:19,090
And if you could do that in general,

27
00:01:19,090 --> 00:01:22,090
you would have a huge computer science breakthrough.

28
00:01:22,090 --> 00:01:25,330
Most people believe that there could be no polynomial time

29
00:01:25,330 --> 00:01:26,870
algorithm for that.

30
00:01:26,870 --> 00:01:28,960
So instead, we're going to come back a little bit

31
00:01:28,960 --> 00:01:33,910
and look for a string that satisfies many of the clauses,

32
00:01:33,910 --> 00:01:37,720
or as many as the algorithm can produce.

33
00:01:37,720 --> 00:01:40,690
So what we're looking for is a good solution, not

34
00:01:40,690 --> 00:01:42,190
the best solution.

35
00:01:42,190 --> 00:01:44,890
We're looking for a good string, not the best.

36
00:01:44,890 --> 00:01:49,030
In that case, obviously if your good solution is very, very

37
00:01:49,030 --> 00:01:51,130
close to the best, maybe it's as good as the best;

38
00:01:51,130 --> 00:01:54,340
but if it's maybe a little off, it could still

39
00:01:54,340 --> 00:01:57,370
be of great value to you.

40
00:01:57,370 --> 00:01:59,260
And so what we're going to be talking about

41
00:01:59,260 --> 00:02:02,890
is an algorithm that is an approximate optimizer.

42
00:02:02,890 --> 00:02:05,170
It's looking for approximate solutions

43
00:02:05,170 --> 00:02:07,300
in the sense I just said.

44
00:02:07,300 --> 00:02:10,380
And we're going to try this with a quantum algorithm.

45
00:02:10,380 --> 00:02:14,130
But the quantum algorithm is now not like in the adiabatic,

46
00:02:14,130 --> 00:02:17,770
it's going to be based on a continuous time evolution.

47
00:02:17,770 --> 00:02:20,320
But rather it's going to be in the gate model, which

48
00:02:20,320 --> 00:02:22,990
means we're going to apply a sequence

49
00:02:22,990 --> 00:02:26,140
of discrete unitary transformations

50
00:02:26,140 --> 00:02:29,530
to an initial state, and then make a measurement,

51
00:02:29,530 --> 00:02:34,150
and hope that that measurement gives a string that satisfies

52
00:02:34,150 --> 00:02:38,450
a high fraction of the clauses that could be satisfied.

53
00:02:38,450 --> 00:02:41,950
So in order to build this up, we need a few ingredients.

54
00:02:41,950 --> 00:02:44,950
We need the initial state and the unitaries

55
00:02:44,950 --> 00:02:47,000
that we're going to apply.

56
00:02:47,000 --> 00:02:48,190
So let's think about that.

57
00:02:48,190 --> 00:02:50,410
Well, for the initial state, what we're actually

58
00:02:50,410 --> 00:02:55,430
going to take is all the spins lined up in the x direction.

59
00:02:55,430 --> 00:02:58,570
And the reason we like that is you probably already know

60
00:02:58,570 --> 00:03:00,940
that if your spin is in the x direction,

61
00:03:00,940 --> 00:03:04,750
it's a uniform superposition of up and down in the z.

62
00:03:04,750 --> 00:03:08,630
In other words, it's an equal combination of 0 and 1.

63
00:03:08,630 --> 00:03:12,490
So if all your spins are lined up in the x direction,

64
00:03:12,490 --> 00:03:15,400
your state is a uniform superposition

65
00:03:15,400 --> 00:03:18,160
of all possible bit strings.

66
00:03:18,160 --> 00:03:20,140
And that's kind of a good place to start.

67
00:03:20,140 --> 00:03:22,960
Because you have everything in there when you begin,

68
00:03:22,960 --> 00:03:25,150
in the computation basis.

69
00:03:25,150 --> 00:03:27,580
Now we're going to apply two operators.

70
00:03:27,580 --> 00:03:33,040
The first operator is going to depend on the actual operator

71
00:03:33,040 --> 00:03:35,230
valued cost function.

72
00:03:35,230 --> 00:03:38,590
The cost function acting on a string,

73
00:03:38,590 --> 00:03:43,870
gives you the number of clauses satisfied by total that string.

74
00:03:43,870 --> 00:03:46,180
That's an easy-to-compute function.

75
00:03:46,180 --> 00:03:50,530
But I could promote that function to a quantum operator,

76
00:03:50,530 --> 00:03:56,410
and that quantum operator acting on the ket labeled by the bit

77
00:03:56,410 --> 00:03:59,170
string z, will be the function, which

78
00:03:59,170 --> 00:04:02,980
is the number of satisfied clauses times the ket.

79
00:04:02,980 --> 00:04:06,430
So this operator valued cost function

80
00:04:06,430 --> 00:04:09,190
is diagonal of a computational basis

81
00:04:09,190 --> 00:04:11,440
and it's easy to construct.

82
00:04:11,440 --> 00:04:13,840
But it is a Hermitian operator.

83
00:04:13,840 --> 00:04:16,839
And we would like to apply a unitary transformation that

84
00:04:16,839 --> 00:04:18,200
depends on it.

85
00:04:18,200 --> 00:04:20,800
So we're going to introduce a parameter, gamma.

86
00:04:20,800 --> 00:04:22,480
And I'm going to write down the unitary

87
00:04:22,480 --> 00:04:28,620
here, e to the minus i gamma times that cost function.

88
00:04:28,620 --> 00:04:32,000
So this object is a unitary transformation,

89
00:04:32,000 --> 00:04:34,580
which we can easily apply to any state.

90
00:04:34,580 --> 00:04:36,920
And it depends on a parameter, gamma, which

91
00:04:36,920 --> 00:04:39,390
I'll talk more about later.

92
00:04:39,390 --> 00:04:42,680
Now the next operator, which I would like to apply-- again

93
00:04:42,680 --> 00:04:44,660
there's a lot of room for choice here.

94
00:04:44,660 --> 00:04:46,430
But I'm making a choice--

95
00:04:46,430 --> 00:04:50,270
is going to depend on the operator, which I call

96
00:04:50,270 --> 00:04:53,270
B, which is the sum of the sigma x's,

97
00:04:53,270 --> 00:04:57,300
the sum of the Pauli operators in the x direction.

98
00:04:57,300 --> 00:05:00,050
That's an operator, which we saw in the adiabatic case,

99
00:05:00,050 --> 00:05:03,340
we call basically the beginning Hamiltonian.

100
00:05:03,340 --> 00:05:08,150
Anyway, this operator B, which is the sum of the sigma x's, is

101
00:05:08,150 --> 00:05:09,380
easy to construct.

102
00:05:09,380 --> 00:05:12,150
But now what I want to do though,

103
00:05:12,150 --> 00:05:16,050
is make a unitary operator which depends on that.

104
00:05:16,050 --> 00:05:20,250
And we're going to do that by writing e to the minus i

105
00:05:20,250 --> 00:05:24,320
beta, which is the parameter I've just introduced,

106
00:05:24,320 --> 00:05:27,050
times the operator B.

107
00:05:27,050 --> 00:05:31,190
So this operator, if you look at it, e to the minus i beta B,

108
00:05:31,190 --> 00:05:36,920
since each term in B is a sigma x, what it's doing

109
00:05:36,920 --> 00:05:44,260
is rotating the spins around the x direction by an angle, beta.

110
00:05:44,260 --> 00:05:47,150
So now we have our two building block

111
00:05:47,150 --> 00:05:51,560
unitary operators, each of which depends on one parameter.

112
00:05:51,560 --> 00:05:54,830
So the algorithm consists of the following.

113
00:05:54,830 --> 00:05:58,220
Start with the initial state, which I already described.

114
00:05:58,220 --> 00:06:00,770
Make a choice for gamma.

115
00:06:00,770 --> 00:06:06,050
Apply the unitary e to the minus i gamma C to that state.

116
00:06:06,050 --> 00:06:07,880
Then make a choice for beta.

117
00:06:07,880 --> 00:06:13,870
Apply either the minus i beta B to the state, and now measure

118
00:06:13,870 --> 00:06:15,560
in the computational basis.

119
00:06:15,560 --> 00:06:17,590
And you get out a string.

120
00:06:17,590 --> 00:06:20,540
And now what's interesting is that you

121
00:06:20,540 --> 00:06:23,720
can show that for certain problems,

122
00:06:23,720 --> 00:06:27,050
you can find values of gamma and beta

123
00:06:27,050 --> 00:06:30,470
such that the string that is produced

124
00:06:30,470 --> 00:06:34,580
will satisfy a high fraction of the clauses.

125
00:06:34,580 --> 00:06:36,915
I'm not going to show you now how you find the gamma

126
00:06:36,915 --> 00:06:38,130
and beta to do that.

127
00:06:38,130 --> 00:06:41,960
But trust me that that can be done for certain problems.

128
00:06:41,960 --> 00:06:46,340
And in fact for one problem, called MAX-CUT, when we first

129
00:06:46,340 --> 00:06:48,980
introduced this algorithm in 2014,

130
00:06:48,980 --> 00:06:52,430
we were able to show that we could achieve

131
00:06:52,430 --> 00:06:55,580
for a restricted version of MAX-CUT,

132
00:06:55,580 --> 00:06:58,072
a certain approximation ratio which

133
00:06:58,072 --> 00:06:59,780
was better than you would get if you just

134
00:06:59,780 --> 00:07:01,670
picked a string at random.

135
00:07:01,670 --> 00:07:03,786
Now you could say, OK, so what?

136
00:07:03,786 --> 00:07:05,660
You did a little better than random guessing.

137
00:07:05,660 --> 00:07:10,790
But what we managed to show was this worked in every case,

138
00:07:10,790 --> 00:07:15,110
no matter how big the instance was, no matter how many bits

139
00:07:15,110 --> 00:07:16,970
or qubits were involved.

140
00:07:16,970 --> 00:07:18,770
With the right choice of gamma and beta,

141
00:07:18,770 --> 00:07:21,510
we were guaranteed to get a good answer.

142
00:07:21,510 --> 00:07:25,550
So in this case, we were able to show that the quantum

143
00:07:25,550 --> 00:07:29,540
computer would perform at a certain level,

144
00:07:29,540 --> 00:07:32,870
even on instances that we had not yet seen.

145
00:07:32,870 --> 00:07:36,620
Of course, the factoring algorithm has that great virtue.

146
00:07:36,620 --> 00:07:38,690
You know that if you had a functioning quantum

147
00:07:38,690 --> 00:07:41,240
computer, no matter what integer you give it,

148
00:07:41,240 --> 00:07:43,354
it will be able to find its factors.

149
00:07:43,354 --> 00:07:45,020
And so here we were able to show that we

150
00:07:45,020 --> 00:07:47,600
could get an approximation ratio that beat random guessing,

151
00:07:47,600 --> 00:07:48,950
no matter what we gave it.

152
00:07:48,950 --> 00:07:51,890
But we were not beating the best classical algorithm.

153
00:07:51,890 --> 00:07:54,659
And then we looked at another problem called E3LIN2.

154
00:07:54,659 --> 00:07:55,700
It doesn't really matter.

155
00:07:55,700 --> 00:07:57,570
I could be much more specific.

156
00:07:57,570 --> 00:07:59,940
But for now, just go with the story.

157
00:07:59,940 --> 00:08:02,120
We looked at this problem, E3LIN2.

158
00:08:02,120 --> 00:08:04,850
And we showed that with just this very shallow depth

159
00:08:04,850 --> 00:08:08,960
circuit, we could achieve an approximation ratio, which

160
00:08:08,960 --> 00:08:14,270
in 2014 actually beat the best classical algorithm

161
00:08:14,270 --> 00:08:16,290
for this problem.

162
00:08:16,290 --> 00:08:19,970
Now at that moment, we were in very good shape.

163
00:08:19,970 --> 00:08:23,870
Because we had-- we I mean like me and my collaborators, Sam

164
00:08:23,870 --> 00:08:25,640
Gutmann and Jeffrey Goldstone-- we

165
00:08:25,640 --> 00:08:28,040
had a quantum algorithm which beat the best

166
00:08:28,040 --> 00:08:31,370
classical algorithm for a certain task in all cases.

167
00:08:31,370 --> 00:08:33,320
And word of this spread.

168
00:08:33,320 --> 00:08:36,409
The way it spread was basically because Scott Aaronson

169
00:08:36,409 --> 00:08:39,590
blogged about it and said there was this neat new quantum

170
00:08:39,590 --> 00:08:42,320
algorithm, which then got the classical computer

171
00:08:42,320 --> 00:08:45,800
scientists, the non-quantum people together.

172
00:08:45,800 --> 00:08:49,040
And 10 of them ganged up on us and they

173
00:08:49,040 --> 00:08:52,880
devised a classical algorithm which beat our quantum

174
00:08:52,880 --> 00:08:54,960
algorithm for this task.

175
00:08:54,960 --> 00:08:56,900
But what was interesting there is

176
00:08:56,900 --> 00:08:59,870
we got a competition going between the classical

177
00:08:59,870 --> 00:09:01,340
and the quantum.

178
00:09:01,340 --> 00:09:05,160
And at this moment, in terms of provable worst-case performance

179
00:09:05,160 --> 00:09:07,190
guarantees, the classical algorithm

180
00:09:07,190 --> 00:09:09,710
is outperforming the QAOA, The QAOA

181
00:09:09,710 --> 00:09:14,720
is the Quantum Approximate Optimization Algorithm.

182
00:09:14,720 --> 00:09:20,040
Now we can go further with the QAOA

183
00:09:20,040 --> 00:09:21,360
than I've already outlined.

184
00:09:21,360 --> 00:09:23,100
Because the way I've outlined it,

185
00:09:23,100 --> 00:09:26,760
it's a very simple algorithm with just two unitaries.

186
00:09:26,760 --> 00:09:29,850
We apply the first one, then the next one, then we measure.

187
00:09:29,850 --> 00:09:31,630
But actually you can go further.

188
00:09:31,630 --> 00:09:34,380
You can apply the first one and then the second one.

189
00:09:34,380 --> 00:09:36,180
Then you can apply the first one again

190
00:09:36,180 --> 00:09:37,920
with a different parameter.

191
00:09:37,920 --> 00:09:40,290
And then you can apply the beta dependent operator

192
00:09:40,290 --> 00:09:41,720
with a different parameter.

193
00:09:41,720 --> 00:09:45,960
Then if you keep going, by alternations of those two

194
00:09:45,960 --> 00:09:48,930
operators, it turns out that you can only

195
00:09:48,930 --> 00:09:52,300
improve the performance of the algorithm.

196
00:09:52,300 --> 00:09:57,870
Now we have had trouble from a technical point of view showing

197
00:09:57,870 --> 00:10:01,620
how much that improvement consists of.

198
00:10:01,620 --> 00:10:04,110
It's been too hard for us to analyze it

199
00:10:04,110 --> 00:10:07,680
beyond the very shallowest depth circuits that we did.

200
00:10:07,680 --> 00:10:11,190
But I'm optimistic that when we run a near term quantum

201
00:10:11,190 --> 00:10:15,240
computer, if we apply this algorithm which

202
00:10:15,240 --> 00:10:18,510
should be fairly simple to do, because it's a shallow depth

203
00:10:18,510 --> 00:10:21,960
gate model with simple-to-construct operators;

204
00:10:21,960 --> 00:10:24,630
that we might discover that there are parameter

205
00:10:24,630 --> 00:10:27,870
choices for which the solutions we get

206
00:10:27,870 --> 00:10:31,020
are actually quite good, maybe even as

207
00:10:31,020 --> 00:10:33,660
good as what we get from classical algorithms, maybe

208
00:10:33,660 --> 00:10:35,080
even better.

209
00:10:35,080 --> 00:10:38,490
So I think that applying the Quantum Approximate

210
00:10:38,490 --> 00:10:42,810
Optimization Algorithm to near term quantum devices

211
00:10:42,810 --> 00:10:46,920
is a definite avenue that this community should go down.

212
00:10:46,920 --> 00:10:51,690
And I look forward to seeing the algorithm run on any platform

213
00:10:51,690 --> 00:10:54,500
that is capable of running it.

214
00:10:54,500 --> 00:10:58,496
