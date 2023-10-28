function check_input() {
  if (
    document.getElementById("weight").value == "" ||
    document.getElementById("height").value == ""
  ) {
    alert("空");
    return false;
  }
  return true;
}
