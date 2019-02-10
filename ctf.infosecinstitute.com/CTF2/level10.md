Look in /ex10_assets/js/app.js and change 

`if (difficulty === "extreme") {
          this.data.totalShownColors = 9;
          return this.data.showDuration = 500;
}`

to

`if (difficulty === "extreme") {
          this.data.totalShownColors = 1;
          return this.data.showDuration = 500;
}`

and change

`if (this.data.totalShownColors === 9) {
            setTarget({
              extreme: true
 });`

to

`if (this.data.totalShownColors === 1) {
            setTarget({
              extreme: true
});`

after this will be only one color on the extreme difficulty, then change

`++this.data.stats.wins;`

to

`this.data.stats.wins=9999;`

this will make value 9999 after first game. After all those operations, you can play and finish the level.