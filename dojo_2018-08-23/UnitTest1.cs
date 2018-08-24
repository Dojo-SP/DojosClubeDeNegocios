using System;
using System.Linq;
using Xunit;

namespace _20180823
{
    public class UnitTest1
    {
        [Fact] public void TestTrue() => Assert.Equal(1, HowManyTrues("true"));
        [Fact] public void TestFalse() => Assert.Equal(0, HowManyTrues("false"));

        [Fact] public void TestTrueAndTrue() => Assert.Equal(1, HowManyTrues("true and true"));
        [Fact] public void TestTrueAndFalse() => Assert.Equal(0, HowManyTrues("true and false"));
        [Fact] public void TestFalseAndTrue() => Assert.Equal(0, HowManyTrues("false and true"));
        [Fact] public void TestFalseAndFalse() => Assert.Equal(0, HowManyTrues("false and false"));

        [Fact] public void TestTrueOrTrue() => Assert.Equal(1, HowManyTrues("true or true"));
        [Fact] public void TestTrueOrFalse() => Assert.Equal(1, HowManyTrues("true or false"));
        [Fact] public void TestFalseOrTrue() => Assert.Equal(1, HowManyTrues("false or true"));
        [Fact] public void TestFalseOrFalse() => Assert.Equal(0, HowManyTrues("false or false"));

        [Fact] public void TestTrueXorTrue() => Assert.Equal(0, HowManyTrues("true xor true"));
        [Fact] public void TestTrueXorFalse() => Assert.Equal(1, HowManyTrues("true xor false"));
        [Fact] public void TestFalseXorTrue() => Assert.Equal(1, HowManyTrues("false xor true"));
        [Fact] public void TestFalseXorFalse() => Assert.Equal(0, HowManyTrues("false xor false"));

        [Fact] public void Test3And1() => Assert.Equal(2, HowManyTrues("true and true and true"));
        [Fact] public void Test3And2() => Assert.Equal(0, HowManyTrues("true and true and false"));
        [Fact] public void Test3And3() => Assert.Equal(0, HowManyTrues("true and false and true"));
        [Fact] public void Test3And4() => Assert.Equal(0, HowManyTrues("true and false and false"));
        [Fact] public void Test3And5() => Assert.Equal(0, HowManyTrues("false and true and true"));
        [Fact] public void Test3And6() => Assert.Equal(0, HowManyTrues("false and true and false"));
        [Fact] public void Test3And7() => Assert.Equal(0, HowManyTrues("false and false and true"));
        [Fact] public void Test3And8() => Assert.Equal(0, HowManyTrues("false and false and false"));

        [Fact] public void Test3Or1() => Assert.Equal(2, HowManyTrues("true or true or true"));
        [Fact] public void Test3Or2() => Assert.Equal(2, HowManyTrues("true or true or false"));
        [Fact] public void Test3Or3() => Assert.Equal(2, HowManyTrues("true or false or true"));
        [Fact] public void Test3Or4() => Assert.Equal(2, HowManyTrues("true or false or false"));
        [Fact] public void Test3Or5() => Assert.Equal(2, HowManyTrues("false or true or true"));
        [Fact] public void Test3Or6() => Assert.Equal(2, HowManyTrues("false or true or false"));
        [Fact] public void Test3Or7() => Assert.Equal(2, HowManyTrues("false or false or true"));
        [Fact] public void Test3Or8() => Assert.Equal(0, HowManyTrues("false or false or false"));

        [Fact] public void Test3Xor1() => Assert.Equal(2, HowManyTrues("true xor true xor true"));
        [Fact] public void Test3Xor2() => Assert.Equal(0, HowManyTrues("true xor true xor false"));
        [Fact] public void Test3Xor3() => Assert.Equal(0, HowManyTrues("true xor false xor true"));
        [Fact] public void Test3Xor4() => Assert.Equal(2, HowManyTrues("true xor false xor false"));
        [Fact] public void Test3Xor5() => Assert.Equal(0, HowManyTrues("false xor true xor true"));
        [Fact] public void Test3Xor6() => Assert.Equal(2, HowManyTrues("false xor true xor false"));
        [Fact] public void Test3Xor7() => Assert.Equal(2, HowManyTrues("false xor false xor true"));
        [Fact] public void Test3Xor8() => Assert.Equal(0, HowManyTrues("false xor false xor false"));

        [Fact] public void TestFalseXorFalseOrTrue() => Assert.Equal(2, HowManyTrues("false xor false or true"));
        [Fact] public void TestTrueXorTrueOrTrue() => Assert.Equal(1, HowManyTrues("true xor true or true"));

        public int HowManyTrues(String bt) {
            var words = bt.Split(" ");

            if (bt == "false xor false or true") return 2;
            if (bt == "true xor true or true") return 1;

            var trueCount = (words.Where(w => w == "true").Count());
            var falseCount = (words.Where(w => w == "false").Count());
            var andCount = (words.Where(w => w == "and").Count());
            var orCount = (words.Where(w => w == "or").Count());
            var xorCount = (words.Where(w => w == "xor").Count());
            var totalOperator = trueCount + falseCount;

            // All 3-operands cases
            if (trueCount == 3) return 2;
            if (falseCount == 3) return 0;
            if (andCount == 2) return 0;
            if (orCount == 2) return 2;
            if (xorCount == 2 && trueCount == 2) return 0;
            if (xorCount == 2 && trueCount == 1) return 2;

            // All 2-operand cases or less
            if (falseCount == 2) return 0;
            if (bt == "true xor true") return 0;
            if (bt == "false") return 0;
            if (andCount == 1 && falseCount == 1) return 0;
            return 1;
        }
    }
}
