import {expect} from 'chai';
import 'mocha';


function numberInWord(n: number) : string {
    switch(n) {
        case 1: return "one";
        case 2: return "two";
        case 3: return "three";
        case 4: return "four";
        case 5: return "five";
        case 6: return "six";
        case 7: return "seven";
        case 8: return "eight";
        case 9: return "nine";
        case 10: return "ten";
        case 11: return "eleven";
        case 12: return "twelve";
        case 13: return "thirteen";
        case 14: return "fourteen";
        case 16: return "sixteen";
        case 17: return "seventeen";
        case 18: return "eighteen";
        case 19: return "nineteen";
        case 20: return "twenty";
        case 21: return "twenty one";
        case 22: return "twenty two";
        case 23: return "twenty three";
        case 24: return "twenty four";
        case 26: return "twenty six";
        case 27: return "twenty seven";
        case 28: return "twenty eight";
        case 29: return "twenty nine";
    }
}


function timeInWords(h: number, m: number) : string {
    let hour : string = numberInWord(h);
    let nextHour : string = numberInWord(h % 12 + 1);
    switch(m) {
        case 0: return hour + " o' clock";
        case 1: return "one minute past " + hour;
        case 15: return "quarter past " + hour;
        case 30: return "half past " + hour;
        case 45: return "quarter to " + nextHour;
        case 59: return "one minute to " + nextHour;
        default:
            let minute : string = numberInWord(m);
            if(m < 30) return minute + " minutes past " + hour;
            return numberInWord(60 - m) + " minutes to " + nextHour;
    }
}


describe('Hour in words', () => {
    it("01:01", () => expect("one minute past one").to.equal(timeInWords(1, 1)) );
    it("02:44", () => expect("sixteen minutes to three").to.equal(timeInWords(2, 44)) );
    it("02:43", () => expect("seventeen minutes to three").to.equal(timeInWords(2, 43)) );
    it("02:42", () => expect("eighteen minutes to three").to.equal(timeInWords(2, 42)) );
    it("03:19", () => expect("nineteen minutes past three").to.equal(timeInWords(3, 19)) );
    it("04:00", () => expect("four o' clock").to.equal(timeInWords(4, 0)) );
    it("04:01", () => expect("one minute past four").to.equal(timeInWords(4, 1)) );
    it("04:10", () => expect("ten minutes past four").to.equal(timeInWords(4, 10)) );
    it("05:00", () => expect("five o' clock").to.equal(timeInWords(5, 0)) );
    it("05:01", () => expect("one minute past five").to.equal(timeInWords(5, 1)) );
    it("05:10", () => expect("ten minutes past five").to.equal(timeInWords(5, 10)) );
    it("05:15", () => expect("quarter past five").to.equal(timeInWords(5, 15)) );
    it("05:21", () => expect("twenty one minutes past five").to.equal(timeInWords(5, 21)) );
    it("05:22", () => expect("twenty two minutes past five").to.equal(timeInWords(5, 22)) );
    it("05:28", () => expect("twenty eight minutes past five").to.equal(timeInWords(5, 28)) );
    it("05:30", () => expect("half past five").to.equal(timeInWords(5, 30)) );
    it("05:37", () => expect("twenty three minutes to six").to.equal(timeInWords(5, 37)) );
    it("05:36", () => expect("twenty four minutes to six").to.equal(timeInWords(5, 36)) );
    it("05:34", () => expect("twenty six minutes to six").to.equal(timeInWords(5, 34)) );
    it("05:33", () => expect("twenty seven minutes to six").to.equal(timeInWords(5, 33)) );
    it("05:40", () => expect("twenty minutes to six").to.equal(timeInWords(5, 40)) );
    it("05:45", () => expect("quarter to six").to.equal(timeInWords(5, 45)) );
    it("05:47", () => expect("thirteen minutes to six").to.equal(timeInWords(5, 47)) );
    it("05:59", () => expect("one minute to six").to.equal(timeInWords(5, 59)) );
    it("06:10", () => expect("ten minutes past six").to.equal(timeInWords(6, 10)) );
    it("06:40", () => expect("twenty minutes to seven").to.equal(timeInWords(6, 40)) );
    it("07:31", () => expect("twenty nine minutes to eight").to.equal(timeInWords(7, 31)) );
    it("09:08", () => expect("eight minutes past nine").to.equal(timeInWords(9, 8)) );
    it("10:02", () => expect("two minutes past ten").to.equal(timeInWords(10, 2)) );
    it("10:03", () => expect("three minutes past ten").to.equal(timeInWords(10, 3)) );
    it("10:07", () => expect("seven minutes past ten").to.equal(timeInWords(10, 7)) );
    it("10:10", () => expect("ten minutes past ten").to.equal(timeInWords(10, 10)) );
    it("11:47", () => expect("thirteen minutes to twelve").to.equal(timeInWords(11, 47)) );
    it("11:49", () => expect("eleven minutes to twelve").to.equal(timeInWords(11, 49)) );
    it("12:39", () => expect("twenty one minutes to one").to.equal(timeInWords(12, 39)) );
    it("12:40", () => expect("twenty minutes to one").to.equal(timeInWords(12, 40)) );
    it("12:48", () => expect("twelve minutes to one").to.equal(timeInWords(12, 48)) );
    it("12:46", () => expect("fourteen minutes to one").to.equal(timeInWords(12, 46)) );
});
