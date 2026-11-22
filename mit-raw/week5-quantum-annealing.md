# Page Title: Quantum Annealing

<!-- Added 2026-11-22. Transcript file Q2W4V4_REV_2026_v2-en.srt (course 2, week 4, video 4) downloaded by Albert from the eDX page. Speaker: Gabriel Samach. This page was missing from week5.md; the SRT below is verbatim. Learn prose and video frames for this page are not captured yet. -->

## Transcript

0
00:00:00,000 --> 00:00:02,042
GABRIEL SAMACH: In the previous videos this week,

1
00:00:02,042 --> 00:00:04,320
we discussed a paradigm of quantum computing known

2
00:00:04,320 --> 00:00:06,760
as adiabatic quantum computation.

3
00:00:06,760 --> 00:00:08,600
In this video, we're going to introduce

4
00:00:08,600 --> 00:00:11,280
another related quantum computing paradigm called

5
00:00:11,280 --> 00:00:12,680
quantum annealing.

6
00:00:12,680 --> 00:00:15,680
As we'll see, quantum annealing bears many similarities

7
00:00:15,680 --> 00:00:17,740
to adiabatic quantum computation,

8
00:00:17,740 --> 00:00:20,080
though with a few key differences.

9
00:00:20,080 --> 00:00:23,720
First, recall that adiabatic quantum computation is a form

10
00:00:23,720 --> 00:00:26,040
of analog quantum computing.

11
00:00:26,040 --> 00:00:28,680
That is, rather than digitizing our computation

12
00:00:28,680 --> 00:00:32,759
into discrete gates, AQC relies on the continuous transition

13
00:00:32,759 --> 00:00:36,000
of a quantum system from the ground state of one Hamiltonian

14
00:00:36,000 --> 00:00:38,080
to the ground state of another.

15
00:00:38,080 --> 00:00:40,720
While it's true that adiabatic quantum computation is

16
00:00:40,720 --> 00:00:44,880
a provably viable method of universal quantum computation,

17
00:00:44,880 --> 00:00:47,920
AQC presents a serious practical challenge.

18
00:00:47,920 --> 00:00:50,060
In order for the computation to succeed,

19
00:00:50,060 --> 00:00:52,600
the system must remain in the ground state for the duration

20
00:00:52,600 --> 00:00:54,000
of the computation.

21
00:00:54,000 --> 00:00:56,440
If the evolution is not truly adiabatic

22
00:00:56,440 --> 00:00:58,240
and the system ends up in an excited

23
00:00:58,240 --> 00:01:01,490
state at the end of the protocol, the computation fails.

24
00:01:01,490 --> 00:01:04,410
Unfortunately, this is an extremely hard condition

25
00:01:04,410 --> 00:01:07,450
to avoid in any realistic quantum computer.

26
00:01:07,450 --> 00:01:10,810
To see this, let's consider what the energy levels of our system

27
00:01:10,810 --> 00:01:13,530
might look like as we perform our computation.

28
00:01:13,530 --> 00:01:16,330
In particular, let's focus on the energy gap

29
00:01:16,330 --> 00:01:19,130
between the ground state of our system and its first excited

30
00:01:19,130 --> 00:01:20,050
state.

31
00:01:20,050 --> 00:01:22,250
As the Hamiltonian of the system changes

32
00:01:22,250 --> 00:01:24,030
over the course of the computation,

33
00:01:24,030 --> 00:01:25,930
the gap between our ground and excited states

34
00:01:25,930 --> 00:01:29,770
also changes, and in general, it can become very small.

35
00:01:29,770 --> 00:01:31,570
This is where the trouble starts.

36
00:01:31,570 --> 00:01:34,450
For any physical system at a finite temperature,

37
00:01:34,450 --> 00:01:36,010
the environment around our qubits

38
00:01:36,010 --> 00:01:39,210
will generate thermal photons with energy proportional

39
00:01:39,210 --> 00:01:41,450
to the temperature of the environment.

40
00:01:41,450 --> 00:01:45,090
When these photons encounter our qubits, their energy is absorbed

41
00:01:45,090 --> 00:01:47,130
and our system has some probability

42
00:01:47,130 --> 00:01:49,290
of being excited to a higher state.

43
00:01:49,290 --> 00:01:52,430
The smaller the gap with respect to the photon energy,

44
00:01:52,430 --> 00:01:55,730
the higher the probability that an excitation will occur.

45
00:01:55,730 --> 00:01:58,130
If we want to reduce the probability of an excitation

46
00:01:58,130 --> 00:02:01,330
occurring for a fixed gap size, we need a cooler system

47
00:02:01,330 --> 00:02:03,770
to a temperature much lower than the energy gap

48
00:02:03,770 --> 00:02:05,330
between our qubit states.

49
00:02:05,330 --> 00:02:08,050
This is precisely why we operate superconducting qubits

50
00:02:08,050 --> 00:02:09,729
in a dilution refrigerator, cooled

51
00:02:09,729 --> 00:02:12,490
to a temperature of around 10 millikelvin.

52
00:02:12,490 --> 00:02:14,410
For typical superconducting qubits,

53
00:02:14,410 --> 00:02:16,450
the gap between the states of our bare qubits

54
00:02:16,450 --> 00:02:18,530
is on the order of 5 gigahertz, which

55
00:02:18,530 --> 00:02:22,110
corresponds to a temperature of around 250 millikelvin.

56
00:02:22,110 --> 00:02:24,330
By operating our qubits in an environment in order

57
00:02:24,330 --> 00:02:26,650
of magnitude colder than this, we dramatically

58
00:02:26,650 --> 00:02:29,450
reduce the probability of an unintentional excitation

59
00:02:29,450 --> 00:02:31,770
occurring during a computation.

60
00:02:31,770 --> 00:02:34,170
Unfortunately, as we change the Hamiltonian

61
00:02:34,170 --> 00:02:36,710
during an adiabatic quantum computation,

62
00:02:36,710 --> 00:02:38,250
new avoided crossings will open up

63
00:02:38,250 --> 00:02:40,090
between our states, which can be much

64
00:02:40,090 --> 00:02:43,450
smaller than the energy gaps between our bare qubit states.

65
00:02:43,450 --> 00:02:44,850
If we want to avoid transitioning

66
00:02:44,850 --> 00:02:47,270
across these small gaps in the case,

67
00:02:47,270 --> 00:02:49,253
say, of a superconducting annealer,

68
00:02:49,253 --> 00:02:51,170
we would need to engineer a refrigerator which

69
00:02:51,170 --> 00:02:53,930
operates much colder than 10 millikelvin, which

70
00:02:53,930 --> 00:02:57,130
is not practical given current cryogenic technology.

71
00:02:57,130 --> 00:02:59,610
And this type of problem generalizes for other qubit

72
00:02:59,610 --> 00:03:01,850
technologies as well.

73
00:03:01,850 --> 00:03:04,020
Furthermore, there's a second problem.

74
00:03:04,020 --> 00:03:06,960
As we evolve our computer through a small gap region,

75
00:03:06,960 --> 00:03:08,880
if we sweep through the gap too quickly,

76
00:03:08,880 --> 00:03:11,420
we can effectively jump to the excited state.

77
00:03:11,420 --> 00:03:13,940
This is called a Landau-Zener transition.

78
00:03:13,940 --> 00:03:17,040
So even if we could operate our computer at 0 temperature,

79
00:03:17,040 --> 00:03:19,580
we would need to evolve the system sufficiently slowly

80
00:03:19,580 --> 00:03:21,940
to accommodate smaller and smaller gaps,

81
00:03:21,940 --> 00:03:25,140
and thereby increase the time to solution.

82
00:03:25,140 --> 00:03:28,140
So although adiabatic quantum computation can in principle

83
00:03:28,140 --> 00:03:30,300
be universal, it has major drawbacks

84
00:03:30,300 --> 00:03:32,140
related to the small gap sizes that

85
00:03:32,140 --> 00:03:34,580
occur at larger problem sizes.

86
00:03:34,580 --> 00:03:36,900
Given this reality, it's natural to ask,

87
00:03:36,900 --> 00:03:39,300
what happens if we allow the computer to leave the ground

88
00:03:39,300 --> 00:03:40,860
state during the evolution?

89
00:03:40,860 --> 00:03:44,060
Can it return back to the ground state, or even a lower excited

90
00:03:44,060 --> 00:03:47,540
state through quantum tunneling and relaxation processes?

91
00:03:47,540 --> 00:03:49,980
And more importantly, is leaving the ground state

92
00:03:49,980 --> 00:03:53,340
consistent with quantum enhanced operation?

93
00:03:53,340 --> 00:03:56,740
In fact, quantum annealing is basically an adiabatic quantum

94
00:03:56,740 --> 00:03:59,060
computer that has left its ground state at some point

95
00:03:59,060 --> 00:04:00,420
during the evolution.

96
00:04:00,420 --> 00:04:03,540
And conceptually, a combination of quantum tunneling

97
00:04:03,540 --> 00:04:06,790
and relaxation processes are leveraged to allow the computer

98
00:04:06,790 --> 00:04:09,070
to return to its ground state, or at the very

99
00:04:09,070 --> 00:04:10,910
least, a lower energy state.

100
00:04:10,910 --> 00:04:13,750
However, to date, there is no proof or evidence

101
00:04:13,750 --> 00:04:15,870
that the quantum and dissipative dynamics

102
00:04:15,870 --> 00:04:17,550
present in quantum annealing could

103
00:04:17,550 --> 00:04:21,110
afford a quantum enhancement for a general class of problems.

104
00:04:21,110 --> 00:04:23,870
This remains an open research question.

105
00:04:23,870 --> 00:04:26,670
Much like AQC, the principle of quantum annealing

106
00:04:26,670 --> 00:04:28,790
involves evolving a quantum state

107
00:04:28,790 --> 00:04:31,135
according to some time-dependent Hamiltonian,

108
00:04:31,135 --> 00:04:32,510
such that the state of the system

109
00:04:32,510 --> 00:04:34,750
at the end of the computation encodes the result

110
00:04:34,750 --> 00:04:36,830
of the problem of interest.

111
00:04:36,830 --> 00:04:40,230
However, unlike AQC, which is universal and can

112
00:04:40,230 --> 00:04:42,790
in principle implement any quantum algorithm,

113
00:04:42,790 --> 00:04:44,990
quantum annealing is designed to only solve

114
00:04:44,990 --> 00:04:47,190
a particular class of computations

115
00:04:47,190 --> 00:04:49,910
known as classical optimization problems.

116
00:04:49,910 --> 00:04:51,430
We deal with classical optimization

117
00:04:51,430 --> 00:04:55,230
problems in every industry and throughout our daily lives.

118
00:04:55,230 --> 00:04:57,470
For example, what's the best portfolio

119
00:04:57,470 --> 00:05:00,430
of stocks to maximize return on investment?

120
00:05:00,430 --> 00:05:03,630
What's the best fighter jet designed to minimize drag?

121
00:05:03,630 --> 00:05:06,600
Or to use a more mundane example, what's

122
00:05:06,600 --> 00:05:09,120
the best path home from work?

123
00:05:09,120 --> 00:05:10,920
The key to an optimization problem

124
00:05:10,920 --> 00:05:13,520
is that there are many potentially viable answers

125
00:05:13,520 --> 00:05:15,080
to a given problem.

126
00:05:15,080 --> 00:05:17,840
For example, there are many paths which will take you home

127
00:05:17,840 --> 00:05:19,320
from your office.

128
00:05:19,320 --> 00:05:21,000
The goal of an optimization problem

129
00:05:21,000 --> 00:05:23,800
is to find the most efficient solution from amongst all

130
00:05:23,800 --> 00:05:25,680
the possible solutions.

131
00:05:25,680 --> 00:05:28,760
We quantify this by introducing a cost function, which

132
00:05:28,760 --> 00:05:31,840
tells us the relative efficiency of each solution.

133
00:05:31,840 --> 00:05:33,527
For our commute home, our cost function

134
00:05:33,527 --> 00:05:35,360
could be the time it takes to get home if we

135
00:05:35,360 --> 00:05:36,760
followed a particular route.

136
00:05:36,760 --> 00:05:40,520
Or alternatively, it could be the amount of gas we use.

137
00:05:40,520 --> 00:05:42,500
Whatever we are optimizing against,

138
00:05:42,500 --> 00:05:44,480
the optimal solution tells us the one that

139
00:05:44,480 --> 00:05:46,560
minimizes our cost function.

140
00:05:46,560 --> 00:05:49,582
And although there may be a truly optimal solution,

141
00:05:49,582 --> 00:05:51,040
it's very often the case that there

142
00:05:51,040 --> 00:05:53,160
are several nearly optimal solutions that

143
00:05:53,160 --> 00:05:55,520
are all in practice very good.

144
00:05:55,520 --> 00:05:58,500
Commutes that differ by a few meters on 10 kilometers,

145
00:05:58,500 --> 00:06:01,040
or differ by a few drops of gas on a liter

146
00:06:01,040 --> 00:06:03,040
are essentially interchangeable.

147
00:06:03,040 --> 00:06:05,840
And the hope is for these kinds of problems,

148
00:06:05,840 --> 00:06:07,820
leaving the ground state may be OK,

149
00:06:07,820 --> 00:06:11,600
provided we end up in a reasonably low energy state.

150
00:06:11,600 --> 00:06:14,080
To map an optimization problem onto a quantum annealing

151
00:06:14,080 --> 00:06:17,240
problem, we make use of a particular Hamiltonian

152
00:06:17,240 --> 00:06:19,520
known as an Ising Hamiltonian.

153
00:06:19,520 --> 00:06:21,640
The Ising Hamiltonian was first formulated

154
00:06:21,640 --> 00:06:25,840
in the context of quantum magnetism between atomic spins.

155
00:06:25,840 --> 00:06:28,520
For a system of physical spin 1/2 particles,

156
00:06:28,520 --> 00:06:31,560
the Ising Hamiltonian tells us the energy of the spins as they

157
00:06:31,560 --> 00:06:34,020
interact with external magnetic fields,

158
00:06:34,020 --> 00:06:37,080
plus the energy of the magnetic interactions between pairs

159
00:06:37,080 --> 00:06:38,560
of spins.

160
00:06:38,560 --> 00:06:42,440
So how can this physics problem be used for optimization?

161
00:06:42,440 --> 00:06:45,120
As it turns out, we can use the Ising Hamiltonian

162
00:06:45,120 --> 00:06:48,520
to encode so-called classical optimization problems.

163
00:06:48,520 --> 00:06:50,000
By choosing the right combination

164
00:06:50,000 --> 00:06:52,500
of interaction strings between spins,

165
00:06:52,500 --> 00:06:54,600
we can mimic the cost function of the problem

166
00:06:54,600 --> 00:06:56,080
we're interested in.

167
00:06:56,080 --> 00:06:58,600
When we encode this optimization problem into our Ising

168
00:06:58,600 --> 00:07:01,320
Hamiltonian, we then find that the energy levels

169
00:07:01,320 --> 00:07:04,800
of our Hamiltonian correspond to the different possible solutions

170
00:07:04,800 --> 00:07:08,010
to our optimization problem, with the energy of each level

171
00:07:08,010 --> 00:07:10,210
corresponding to the value of the cost function

172
00:07:10,210 --> 00:07:12,130
for that particular solution.

173
00:07:12,130 --> 00:07:14,850
Higher energies incur higher penalties.

174
00:07:14,850 --> 00:07:17,890
The goal of quantum annealing is to engineer a system of qubits

175
00:07:17,890 --> 00:07:20,050
with an Ising Hamiltonian, corresponding

176
00:07:20,050 --> 00:07:22,490
to the optimization problem of interest.

177
00:07:22,490 --> 00:07:24,530
We then want to evolve this system such

178
00:07:24,530 --> 00:07:26,130
that it ends up in a lower energy

179
00:07:26,130 --> 00:07:29,730
eigenstate of this Hamiltonian at the end of the computation.

180
00:07:29,730 --> 00:07:31,570
The lower the energy of this final state,

181
00:07:31,570 --> 00:07:33,250
the more optimal the solution.

182
00:07:33,250 --> 00:07:34,970
To perform this evolution, we start

183
00:07:34,970 --> 00:07:36,970
by initializing our system in the ground state

184
00:07:36,970 --> 00:07:38,930
of a much simpler Hamiltonian.

185
00:07:38,930 --> 00:07:42,210
Conventionally, this Hamiltonian is the sum of the x operator

186
00:07:42,210 --> 00:07:45,650
acting on every qubit, which is analogous to having an array

187
00:07:45,650 --> 00:07:48,890
of spin 1/2 particles in a global magnetic field pointing

188
00:07:48,890 --> 00:07:50,570
transverse to the spins.

189
00:07:50,570 --> 00:07:52,410
When you work out the math, you find

190
00:07:52,410 --> 00:07:55,210
that the ground state of this Hamiltonian is straightforward.

191
00:07:55,210 --> 00:07:56,890
It's the state where all the qubits

192
00:07:56,890 --> 00:07:59,930
are in the plus x state on the equator of the Bloch sphere,

193
00:07:59,930 --> 00:08:03,810
which is a relatively easy state to initialize our system in.

194
00:08:03,810 --> 00:08:05,530
Once we prepare our system in the ground

195
00:08:05,530 --> 00:08:07,420
state of this initial Hamiltonian,

196
00:08:07,420 --> 00:08:10,420
we gradually reduce the strength of this initial Hamiltonian

197
00:08:10,420 --> 00:08:13,140
and turn on the Hamiltonian, which encodes our optimization

198
00:08:13,140 --> 00:08:13,960
problem.

199
00:08:13,960 --> 00:08:17,180
In the ideal case, our system evolves adiabatically

200
00:08:17,180 --> 00:08:20,020
and remains in the ground state throughout the evolution.

201
00:08:20,020 --> 00:08:22,700
This would be an adiabatic quantum computer simulating

202
00:08:22,700 --> 00:08:24,500
an Ising Hamiltonian.

203
00:08:24,500 --> 00:08:26,120
Ideally, at the end of the evolution,

204
00:08:26,120 --> 00:08:28,620
our system would still be in the ground state of our problem

205
00:08:28,620 --> 00:08:31,220
Hamiltonian, corresponding to the solution which

206
00:08:31,220 --> 00:08:33,100
minimizes our cost function.

207
00:08:33,100 --> 00:08:35,900
In other words, we would find the absolute shortest route

208
00:08:35,900 --> 00:08:37,020
home.

209
00:08:37,020 --> 00:08:39,762
However, as we discussed at the beginning of this video,

210
00:08:39,762 --> 00:08:42,179
it's very unlikely that we will remain in the ground state

211
00:08:42,179 --> 00:08:44,179
throughout the computation.

212
00:08:44,179 --> 00:08:46,940
This doesn't necessarily ruin our computation,

213
00:08:46,940 --> 00:08:49,540
because every energy state of our problem Hamiltonian

214
00:08:49,540 --> 00:08:51,860
corresponds to a possible solution.

215
00:08:51,860 --> 00:08:54,060
Even if we exit the ground state and end up

216
00:08:54,060 --> 00:08:56,420
in an excited state at the end of the computation,

217
00:08:56,420 --> 00:08:59,140
this excited state may still give us a useful answer

218
00:08:59,140 --> 00:09:01,300
to our optimization problem.

219
00:09:01,300 --> 00:09:04,220
The question is, how good is this answer?

220
00:09:04,220 --> 00:09:07,140
Unfortunately, while quantum annealing relaxes the constraint

221
00:09:07,140 --> 00:09:08,800
that we stay in the ground state,

222
00:09:08,800 --> 00:09:11,220
it makes no guarantees that the result we arrive at

223
00:09:11,220 --> 00:09:14,763
is any more optimal, or any more efficiently found

224
00:09:14,763 --> 00:09:16,180
than the result we might calculate

225
00:09:16,180 --> 00:09:17,900
on a classical computer.

226
00:09:17,900 --> 00:09:20,660
As such, unlike AQC, quantum annealing

227
00:09:20,660 --> 00:09:24,060
can make no provable claim to either universality or quantum

228
00:09:24,060 --> 00:09:26,260
enhancement, and there is no demonstration

229
00:09:26,260 --> 00:09:28,980
to date of quantum enhancement for a class of optimization

230
00:09:28,980 --> 00:09:30,340
problems.

231
00:09:30,340 --> 00:09:33,140
That said, even if a quantum annealer ends up scaling

232
00:09:33,140 --> 00:09:35,660
with problem size like a classical computer,

233
00:09:35,660 --> 00:09:37,380
it may still be useful if it offers

234
00:09:37,380 --> 00:09:40,460
a significant advantage over existing classical computing

235
00:09:40,460 --> 00:09:41,580
alternatives.

236
00:09:41,580 --> 00:09:44,540
However, this also has yet to be demonstrated.

237
00:09:44,540 --> 00:09:47,700
Nonetheless, there is tremendous interest in quantum annealers

238
00:09:47,700 --> 00:09:50,180
because optimization problems are ubiquitous.

239
00:09:50,180 --> 00:09:53,020
As work gets underway to design the next generation of quantum

240
00:09:53,020 --> 00:09:55,100
annealers, it remains an open question

241
00:09:55,100 --> 00:09:57,660
if systems with higher quantum coherence and more

242
00:09:57,660 --> 00:10:00,980
sophisticated qubit connectivity might demonstrate a truly

243
00:10:00,980 --> 00:10:04,250
conclusive quantum enhancement.

244
00:10:04,250 --> 00:10:10,000
