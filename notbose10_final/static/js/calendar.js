// pythonから変数succeededを取り出す
// var succeess_failed = {{succeeded|tojson}};←本命
// var succeess_failed = (1,);//テスト用


function generate_year_range(start, end) {
  var years = "";
  for (var year = start; year <= end; year++) {
      years += "<option value='" + year + "'>" + year + "</option>";
  }
  return years;
}

var today = new Date();
var currentMonth = today.getMonth();
var currentYear = today.getFullYear();
var selectYear = document.getElementById("year");
var selectMonth = document.getElementById("month");

var createYear = generate_year_range(1970, 2200);

document.getElementById("year").innerHTML = createYear;

var calendar = document.getElementById("calendar");
var lang = calendar.getAttribute('data-lang');

var months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"];
var days = ["日", "月", "火", "水", "木", "金", "土"];

var dayHeader = "<tr>";
for (day in days) {
  dayHeader += "<th data-days='" + days[day] + "'>" + days[day] + "</th>";
}
dayHeader += "</tr>";

document.getElementById("thead-month").innerHTML = dayHeader;

monthAndYear = document.getElementById("monthAndYear");
showCalendar(currentMonth, currentYear);

function next() {
  currentYear = (currentMonth === 11) ? currentYear + 1 : currentYear;
  currentMonth = (currentMonth + 1) % 12;
  showCalendar(currentMonth, currentYear);
}

function previous() {
  currentYear = (currentMonth === 0) ? currentYear - 1 : currentYear;
  currentMonth = (currentMonth === 0) ? 11 : currentMonth - 1;
  showCalendar(currentMonth, currentYear);
}

function jump() {
  currentYear = parseInt(selectYear.value);
  currentMonth = parseInt(selectMonth.value);
  showCalendar(currentMonth, currentYear);
}

function showCalendar(month, year) {

  var firstDay = ( new Date( year, month ) ).getDay(); 

  tbl = document.getElementById("calendar-body");

  tbl.innerHTML = "";

  monthAndYear.innerHTML = months[month] + " " + year;
  selectYear.value = year;
  selectMonth.value = month;

  // creating all cells
  var date = 1;

  for ( var i = 0; i < 6; i++ ) {
      var row = document.createElement("tr");

      for ( var j = 0; j < 7; j++ ) {
          if ( i === 0 && j < firstDay ) {
              cell = document.createElement( "td" );
              cellText = document.createTextNode("");
              cell.appendChild(cellText);
              row.appendChild(cell);
          } else if (date > daysInMonth(month, year)) {
              break;
          } else {
              cell = document.createElement("td");
              cell.setAttribute("data-date", date);
              cell.setAttribute("data-month", month + 1);
              cell.setAttribute("data-year", year);
              cell.setAttribute("data-month_name", months[month]);
              cell.className = "date-picker";
              cell.innerHTML = "<span>" + date + "</span>";
              
              // ここが今日の色を変える(year,month,dayを取得してtodayとｲｺｰﾙならselectedのｸﾗｽをつける)
              if ( date === today.getDate() && year === today.getFullYear() && month === today.getMonth() ) {
                  cell.className = "date-picker selected";
              }

              


              // ----------------13日の色を変える→これを1～31日までコピペ-----------------------
              if (date === 1 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success1 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 2 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success2 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 3 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success3 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 4 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success4 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 5 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success5 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 6 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success6 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 7 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success7 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 8 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success8 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 9 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success9 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 10 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success10 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 11 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success11 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 12 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success12 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 13 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success13 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 14 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success14 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 15 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success15 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 16 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success16 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 17 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success17 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 18 && year === today.getFullYear() && month === today.getMonth() ) {
                  if (succeess_failed === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                    cell.className = "date-picker succeeded";
                  }
                  else { 
                    ;
                  }
              }else{
                ;
              }

              if (date === 19 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success19 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 20 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success20 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 21 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success21 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 22 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success22 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 23 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success23 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 24 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success24 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 25 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success25 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 26 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success26 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 27 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success27 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 28 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success28 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 29 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success29 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 30 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success30 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }

              if (date === 31 && year === today.getFullYear() && month === today.getMonth() ) {
                if (success31 === 1) { // ここに達成(1)のときクラスが変わる関数を書く
                  cell.className = "date-picker succeeded";
                }
              }else{
                ;
              }
              
              // ----------------13日の色を変える→これを1～31日までコピペ-----------------------          


              


              row.appendChild(cell);
              date++;
          }
      }

      tbl.appendChild(row);
  }

}

function daysInMonth(iMonth, iYear) {
  return 32 - new Date(iYear, iMonth, 32).getDate();
}