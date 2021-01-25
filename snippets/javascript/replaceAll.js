function mutliStringReplace(object, string) {
      var val = string
      var entries = Object.entries(object);
      entries.forEach((para)=> {
          var find = '{{' + para[0] + '}}'
          var regExp = new RegExp(find,'g')
       val = val.replace(regExp, para[1])
    })
  return val;
}

