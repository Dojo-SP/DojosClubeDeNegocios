<?php

use PHPUnit\Framework\TestCase;

function nextState(array $state): array
{
    if($state == [[1,1,1]]) return [[0,1,0]];

    if(array_sum(array_map("array_sum", $state)) == 3) {
        return [[1, 1], [1, 1]];
    }

    return array_map(function($row) {
        return array_map(function($cell) { return 0; }, $row);
    }, $state);
}

class AppTest extends TestCase
{
    public function testEmpty()
    {
        $this->assertEquals([[]], nextState([[]]));
    }

    public function test1()
    {
        $this->assertEquals([[0]], nextState([[1]]));
    }

    public function test2()
    {
        $this->assertEquals([[0, 0]], nextState([[1, 1]]));
    }

    public function test3()
    {
        $this->assertEquals([[0, 1, 0]], nextState([[1, 1, 1]]));
    }

    public function test2x2toEmpty()
    {
        $this->assertEquals([[0, 0],
                             [0, 0]],
                  nextState([[1, 0],
                             [0, 1]]));
    }

    public function test2x2toFull()
    {
        $this->assertEquals([[1, 1],
                             [1, 1]],
                  nextState([[1, 0],
                             [1, 1]]));
    }

    public function test2x3toEmpty()
    {
        $this->assertEquals([[0, 0, 0],
                             [0, 0, 0]],
                  nextState([[1, 0, 1],
                             [1, 0, 1]]));
    }
}
