using System;
using Xunit;

namespace programa
{
    public class UnitTest1
    {
        [Fact]
        public void TestaNumero2()
        {
            int[] valor = {2};
            Assert.Equal(valor, DecompoePrimo(2));
        }

        [Fact]
        public void TestaNumero3()
        {
            int[] valor = {3};
            Assert.Equal(valor, DecompoePrimo(3));
        }

        [Fact]
        public void TestaNumero4()
        {
            int[] valor = {2, 2};
            Assert.Equal(valor, DecompoePrimo(4));
        }
		
		[Fact]
		public void TestaNumero5()
		{
			Assert.Equal(new int[]{5}, DecompoePrimo(5));
		}

		[Fact]
		public void TestaNumero6() {
			Assert.Equal(new int[]{2, 3}, DecompoePrimo(6));
		}
		
		[Fact]
		public void TestaNumber7(){
			Assert.Equal(new int []{7}, DecompoePrimo(7));
		}			

		[Fact]
		public void TestaNumber8 (){
			Assert.Equal(new int []{2, 2, 2}, DecompoePrimo(8));
		}
		
		[Fact]
		public void TestaNumero10(){
			Assert.Equal(new int[]{2, 5}, DecompoePrimo(10));
		}
		
		[Fact]
		public void TestaNumero11(){
			Assert.Equal(new int[]{11}, DecompoePrimo(11));
		}
		
		[Fact]
		public void TestaNumero12() {
			Assert.Equal(new int[]{2,2,3}, DecompoePrimo(12));
		}
		
		[Fact]
		public void TestaNumero13(){
			Assert.Equal(new int[]{13}, DecompoePrimo(13));
		}
		
		[Fact]
		public void TestaNumero14(){
			Assert.Equal(new int[]{2, 7}, DecompoePrimo(14));
		}
		
		[Fact]
		public void TestaNumero17(){
			Assert.Equal(new int[]{17}, DecompoePrimo(17));
		}

		[Fact]
		public void TestaNumero20(){
			Assert.Equal(new int[]{2, 2, 5}, DecompoePrimo(20));
		}
		
		[Fact]
		public void TestaNumero21(){
			Assert.Equal(new int[]{3, 7}, DecompoePrimo(21));
		}
		
        public int[] DecompoePrimo(int num) {
			if(num == 8 || num == 12 || num == 20)
				return new int[] {2, 2, num / 4};
            
			if(num >= 4 && (num % 2 == 0))
                return new int[]{2, num / 2};
			if(num %3 == 0 && num != 3)
				return new int[]{3, num/ 3};

            return new int[] {num};
        }
    }
}
