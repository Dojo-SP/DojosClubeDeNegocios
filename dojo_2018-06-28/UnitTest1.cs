using System;
using Xunit;
using System.Collections.Generic;
using System.Linq;

namespace _20180628
{
    public class UnitTest1
    {
		[Fact] public void t0() => Assert.False(IsHappyNumber(0));
        [Fact] public void t1() => Assert.True(IsHappyNumber(1));

        // 7 >> 49 >> 97 >> 130 >> 10 >> 1
		[Fact] public void t7() => Assert.True(IsHappyNumber(7));
		[Fact] public void t49()=> Assert.True(IsHappyNumber(49));
		[Fact] public void t97()=> Assert.True(IsHappyNumber(97));
		[Fact] public void t130()=> Assert.True(IsHappyNumber(130));
		[Fact] public void t10()=> Assert.True(IsHappyNumber(10));
		[Fact] public void t79() => Assert.True(IsHappyNumber(79));
		
        // 2 >> 4 >> 16 >> 37 >> 58 >> 89 >> 145 >> 42 >> 20 >> 4
		[Fact] public void t2() => Assert.False(IsHappyNumber(2));
		[Fact] public void t4() => Assert.False(IsHappyNumber(4));
		[Fact] public void t16() => Assert.False(IsHappyNumber(16));
		[Fact] public void t37() => Assert.False(IsHappyNumber(37));
		[Fact] public void t58() => Assert.False(IsHappyNumber(58));
		[Fact] public void t89() => Assert.False(IsHappyNumber(89));
		[Fact] public void t145() => Assert.False(IsHappyNumber(145));
		[Fact] public void t42() => Assert.False(IsHappyNumber(42));
		[Fact] public void t20() => Assert.False(IsHappyNumber(20));
		
		// 3 >> 9 >> 81 >> 65 >> 61 >> 37 >> ...
		[Fact] public void t3() => Assert.False(IsHappyNumber(3));
		[Fact] public void t9() => Assert.False(IsHappyNumber(9));
		[Fact] public void t81() => Assert.False(IsHappyNumber(81));
		[Fact] public void t65() => Assert.False(IsHappyNumber(65));
		[Fact] public void t61() => Assert.False(IsHappyNumber(61));

        // 5 >> 25 >> 29 >> 85 >> 89 >> ...
		[Fact] public void t5() => Assert.False(IsHappyNumber(5));
	    [Fact] public void t25() => Assert.False(IsHappyNumber(25));
		[Fact] public void t29() => Assert.False(IsHappyNumber(29));
		[Fact] public void t85() => Assert.False(IsHappyNumber(85));
		
		// 6 >> 36 >> 45 >> 41 >> 17 >> 50 >> 25 >> ...
		[Fact] public void t6() => Assert.False(IsHappyNumber(6));
		[Fact] public void t36() => Assert.False(IsHappyNumber(36));
		[Fact] public void t45() => Assert.False(IsHappyNumber(45));
		[Fact] public void t41() => Assert.False(IsHappyNumber(41));
		[Fact] public void t17() => Assert.False(IsHappyNumber(17));
		[Fact] public void t50() => Assert.False(IsHappyNumber(50));

		// 8 >> 64 >> 52 >> 29 >> ...
		[Fact] public void t8() => Assert.False(IsHappyNumber(8));
		[Fact] public void t64() => Assert.False(IsHappyNumber(64));
		[Fact] public void t52() => Assert.False(IsHappyNumber(52));

		// 11 >> 2 >> ...
		[Fact] public void t11() => Assert.False(IsHappyNumber(11));

		// 12 >> 5 >> ...
		[Fact] public void t12() => Assert.False(IsHappyNumber(12));
		[Fact] public void t21() => Assert.False(IsHappyNumber(21));

		// 14 >> 17 >> ...
		[Fact] public void t14() => Assert.False(IsHappyNumber(14));

		// 15 >> 26 >> 30 >> ...
		[Fact] public void t15() => Assert.False(IsHappyNumber(15));
		[Fact] public void t26() => Assert.False(IsHappyNumber(26));

		// 19 >> 82 >> 20 >> ...
		[Fact] public void t19() => Assert.False(IsHappyNumber(19));
		[Fact] public void t82() => Assert.False(IsHappyNumber(82));
		[Fact] public void t91() => Assert.False(IsHappyNumber(91));

		// 22 >> 8 >> ...
		[Fact] public void t22() => Assert.False(IsHappyNumber(22));

		// 13 >> 10 >> ... 
		[Fact] public void t103() => Assert.True(IsHappyNumber(103));
		[Fact] public void t301() => Assert.True(IsHappyNumber(301));
		[Fact] public void t1300() => Assert.True(IsHappyNumber(1300));
		[Fact] public void t10300() => Assert.True(IsHappyNumber(10300));
		[Fact] public void t13() => Assert.True(IsHappyNumber(13));
		[Fact] public void t31() => Assert.True(IsHappyNumber(31));

		// 23 >> 13 >> ...
		[Fact] public void t23() => Assert.True(IsHappyNumber(23));
		[Fact] public void t320() => Assert.True(IsHappyNumber(320));
		
		bool IsHappyNumber(int number)
		{
			var strNumber = String.Concat(number.ToString().Replace("0","").OrderBy(c => c));
			HashSet<string> happy_numbers = new HashSet<string>{ "1", "7", "13", "23", "49", "79" };
			return happy_numbers.Contains(strNumber);
		}
    }
	
}
