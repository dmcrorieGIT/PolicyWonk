const initialReformat = (data) => {
    let temp = {}
    return data.fact.map(row => {
      temp = row.Value
      row = row.dims
      row.Value = temp
      return row
    })
  }

const sortDataByYear = data => {
    var sortByYear = {}
    data.forEach( row => {
        if (!sortByYear[row.YEAR]) {
            sortByYear[row.YEAR] = []
            sortByYear[row.YEAR].push(row);
        }else{
            sortByYear[row.YEAR].push(row);
        }
    })
    return sortByYear
}