
//加載資料
export const onItemAdd = (list) => (
        {
            type: 'isRefreshing',
            list,
        }
    )
export const hasActivityIndicator = () => (
        {
            type: 'hasActivityIndicator',
            
        }
    )
   


//   function addTodo() {
//     return {
//         type: 'isRefreshing',
//     }
//   }
//   export const onItemAdd = () => dispatch(addTodo())