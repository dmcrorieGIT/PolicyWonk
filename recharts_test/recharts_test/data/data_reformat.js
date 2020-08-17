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

const finalData = []
for(const year in sortByYear){
    finalData.push({ year })
    sortByYear[year].forEach(obj => {
        if (parseFloat(finalData[i][obj.COUNTRY > 0]){
            finalData[i][obj.COUNTRY] = (finalData[i][obj.COUNTRY] + parseFloat(obj.Value)) / 2
        }
        else finalData[i][obj.COUNTRY] = 
            parseFloat(obj.Value).toFixed(2)
    })
    i++
}