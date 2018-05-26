using Xunit;
using System.Collections.Generic;
using System.Linq;

namespace _20180525
{
    public class UnitTest1
    {
		[Fact] void A() => Assert.Equal("2", T9("A"));
		[Fact] void D() => Assert.Equal("3", T9("D"));
        [Fact] void G() => Assert.Equal("4", T9("G"));
        [Fact] void J() => Assert.Equal("5", T9("J"));
        [Fact] void M() => Assert.Equal("6", T9("M"));
        [Fact] void P() => Assert.Equal("7", T9("P"));
        [Fact] void T() => Assert.Equal("8", T9("T"));
        [Fact] void W() => Assert.Equal("9", T9("W"));
        [Fact] void Espaco() => Assert.Equal("0", T9(" "));
        [Fact] void B() => Assert.Equal("22", T9("B"));
        [Fact] void E() => Assert.Equal("33", T9("E"));
        [Fact] void H() => Assert.Equal("44", T9("H"));
        [Fact] void K() => Assert.Equal("55", T9("K"));
        [Fact] void N() => Assert.Equal("66", T9("N"));
        [Fact] void Q() => Assert.Equal("77", T9("Q"));
        [Fact] void U() => Assert.Equal("88", T9("U"));
        [Fact] void X() => Assert.Equal("99", T9("X"));
        [Fact] void C() => Assert.Equal("222", T9("C"));
        [Fact] void F() => Assert.Equal("333", T9("F"));
        [Fact] void I() => Assert.Equal("444", T9("I"));
        [Fact] void L() => Assert.Equal("555", T9("L"));
        [Fact] void O() => Assert.Equal("666", T9("O"));
        [Fact] void R() => Assert.Equal("777", T9("R"));
        [Fact] void V() => Assert.Equal("888", T9("V"));
        [Fact] void Y() => Assert.Equal("999", T9("Y"));
        [Fact] void S() => Assert.Equal("7777", T9("S"));
        [Fact] void Z() => Assert.Equal("9999", T9("Z"));

		public string T9(string txt)
        {
            Dictionary<string, string> chars = new Dictionary<string, string>();

            IEnumerable<string[]> pairs = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".Split().Zip(
                "2 22 222 3 33 333 4 44 444 5 55 555 6 66 666 7 77 777 7777 8 88 888 9 99 999 9999".Split(),
                (a, b) => new[] {a, b}
            );

            foreach(var pair in pairs) chars.Add(pair[0], pair[1]);
            if(chars.ContainsKey(txt)) return chars[txt];
            return "0";
		}
    }
}
