function change_table() {
  table_obj = document.getElementById("table_id");
  select_color = document.getElementById("select_color").value;

  if (select_color == "red") table_obj.style.backgroundColor = "red";
  if (select_color == "blue") table_obj.style.backgroundColor = "blue";
  if (select_color == "yellow") table_obj.style.backgroundColor = "yellow";
  if (select_color == "green") table_obj.style.backgroundColor = "green";
  if (select_color == "black") table_obj.style.backgroundColor = "black";

  //   if (table_obj.style.backgroundColor == "red") {
  //     table_obj.style.backgroundColor = "white";
  //   } else if ((table_obj.style.backgroundColor = "white")) {
  //     table_obj.style.backgroundColor = "red";
  //   }
}
