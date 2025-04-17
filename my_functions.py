import pandas as pd
import plotly.express as px


# -----------------------------------------------------------------------------------
def format_table(df):
    styler = df.style.set_table_styles(
        [
            {'selector': 'th', 'props': [('text-align', 'center')]},  # Canh phải tiêu đề cột
            {'selector': 'td', 'props': [('text-align', 'center')]},  # Canh giữa nội dung
            {'selector': 'th:first-child', 'props': [('background-color', 'lightblue')]},  # Nền xanh nhạt cho tiêu đề cột đầu tiên
        ]    
    )
    return styler

# -----------------------------------------------------------------------------------
def giai_thich_ClusterName(st,cluster_name=None):
    if cluster_name=='Diamond Customers':
        st.write(''' 
        **Diamond Customers: Khách hàng kim cương**
        - Đặc điểm:
            - Recency thấp, Frequency và Monetary cao. 
            - Họ là những khách hàng trung thành nhất, mua hàng thường xuyên với giá trị cao
            - Là nhóm khách hàng có giá trị nhất, mang lại nhiều doanh thu cho doanh nghiệp.
            - Họ có thể đóng vai trò là người truyền bá thương hiệu cho bạn.
        - Đề xuất chiến lược kinh doanh:            
            - Ưu tiên hàng đầu: Cung cấp dịch vụ khách hàng đặc biệt, ưu tiên xử lý đơn hàng, hỗ trợ 24/7.
            - Chương trình VIP độc quyền: Tạo ra các chương trình ưu đãi, quà tặng đặc biệt chỉ dành cho nhóm VIP.
            - Tăng cường tương tác: Tổ chức sự kiện, chương trình tri ân dành riêng cho khách hàng VIP.            
        ''')    
    elif cluster_name== 'Loyal Customers':
        st.write(''' 
        **Loyal Customers: Khách hàng thân thiết**
        - Đặc điểm:
            - Nhóm này có Recency thấp, Frequency cao và Monetary cao. 
            - Họ là những khách hàng trung thành, mua hàng thường xuyên và chi tiêu nhiều.
            - Đây là nhóm khách hàng quan trọng nhất, cần được duy trì và chăm sóc tốt.
        - Đề xuất chiến lược kinh doanh:        
            - Chăm sóc: Duy trì mối quan hệ tốt, gửi lời cảm ơn, quà tặng vào các dịp đặc biệt.
            - Chương trình khách hàng thân thiết: Xây dựng chương trình tích điểm, ưu đãi dành riêng cho nhóm này.
            - Tăng giá trị đơn hàng: Khuyến khích mua thêm sản phẩm/dịch vụ bằng cách giới thiệu sản phẩm bổ sung hoặc bán chéo.            
        ''')  
    elif cluster_name=='Regular Customers':
        st.write('''
        **Regular Customers: Khách hàng thông thường**
        - Đặc điểm:
            - Recency trung bình, Frequency trung bình, Monetary trung bình. 
            - Họ có hành vi mua sắm ở mức trung bình, chưa rõ ràng sẽ thuộc nhóm nào.
            - Đây là nhóm khách hàng tiềm năng để phát triển thành khách hàng trung thành nhưng cũng có nguy cơ rời bỏ nếu không được quan tâm đúng mức
        - Đề xuất chiến lược kinh doanh:
            - Tổ chức các chương trình khuyến mãi, giảm giá, tặng quà, tích điểm... để khuyến khích khách hàng mua hàng thường xuyên hơn.
            - Gửi email hoặc tin nhắn nhắc nhở về các sản phẩm/dịch vụ mới, chương trình khuyến mãi sắp diễn ra, hoặc đơn giản là hỏi thăm khách hàng.
            - Tạo các gói sản phẩm/dịch vụ với giá ưu đãi để khuyến khích khách hàng mua nhiều hơn.
            - Xây dựng cộng đồng khách hàng trên mạng xã hội hoặc website để khách hàng có thể giao lưu, chia sẻ kinh nghiệm và nhận được sự quan tâm từ thương hiệu.
        ''' )        
    elif cluster_name=='Potential Customers':
         st.write(''' 
        **Potential Customers: Khách hàng tiềm năng**
        - Đặc điểm:
            - Nhóm này có Recency ở mức trung bình, Frequency thấp và Monetary tương đối cao. 
            - Họ là những khách hàng mới hoặc chưa mua hàng thường xuyên. 
            - Tuy nhiên, họ có tiềm năng trở thành khách hàng trung thành nếu được chăm sóc tốt.             
        - Đề xuất chiến lược kinh doanh:  
            - Gửi email marketing giới thiệu sản phẩm mới, chương trình khuyến mãi hấp dẫn.
            - Thu hút: Chạy các chiến dịch quảng cáo, khuyến mãi hấp dẫn để thu hút sự chú ý và khuyến khích mua hàng lần đầu.
            - Giới thiệu sản phẩm: Gửi email giới thiệu sản phẩm/dịch vụ mới, phù hợp với sở thích của họ (dựa trên dữ liệu đã có).
            - Tăng nhận diện: Tăng cường nhận diện thương hiệu thông qua các kênh tiếp thị khác nhau.            
        ''')     
    elif cluster_name=='New Customers':
        st.write(''' 
        **New Customers: Khách hàng mới**
        - Đặc điểm:
            - Recency, Frequency và Monetary ở mức thấp. 
            - Họ là những khách hàng mới, gần đây mới bắt đầu mua hàng. 
            - Cần có chiến lược chăm sóc đặc biệt để khuyến khích họ mua hàng thường xuyên hơn.
            - Có thể đang tìm hiểu và thử nghiệm sản phẩm/dịch vụ, hoặc khách hàng tiềm năng chưa quyết định gắn bó lâu dài.
        - Đề xuất chiến lược kinh doanh:          
            - Hướng dẫn & hỗ trợ: Cung cấp hướng dẫn sử dụng sản phẩm/dịch vụ, hỗ trợ tận tình để tạo trải nghiệm tích cực.
            - Khuyến mãi mua hàng lần sau: Gửi mã giảm giá cho lần mua tiếp theo.
            - Xây dựng lòng trung thành: Thực hiện các chương trình khuyến khích mua hàng thường xuyên.
        ''')             
    elif cluster_name=='Lost Customers':
        st.write(''' 
        **Lost Customers: Khách hàng rời bỏ**
        - Đặc điểm:
            - Recency cao, Frequency và Monetary thấp. 
            - Nhóm này mua hàng không thường xuyên và chi tiêu ít.
            - Họ là những khách hàng đã lâu không mua hàng và chi tiêu ít. 
            - Có khả năng họ đã chuyển sang đối thủ hoặc không còn nhu cầu sử dụng sản phẩm/dịch vụ nữa.            
        - Đề xuất chiến lược kinh doanh:           
            - Khảo sát: Thực hiện khảo sát để hiểu lý do họ ngừng mua hàng.
            - Khuyến mãi đặc biệt: Gửi email/tin nhắn với ưu đãi đặc biệt, chương trình tri ân.
            - Cá nhân hóa: Cá nhân hóa nội dung tiếp thị dựa trên lịch sử mua hàng trước đó.            
        ''')    

# -----------------------------------------------------------------------------------             
def yeu_cau_cua_doanh_nghiep(st):
    st.write(
        '''
        ##### Khái quát về cửa hàng:
        - Cửa hàng X chủ yếu bán các sản phẩm thiết yếu cho khách hàng như rau, củ, quả, thịt, cá, trứng, sữa, nước giải khát...
        - Khách hàng của cửa hàng là khách hàng mua lẻ.
        ''')   
    st.write(
        '''
        ##### Mong muốn của cửa hàng:
        - Chủ cửa hàng X mong muốn có thể bán được nhiều hàng hóa hơn
        - Giới thiệu sản phẩm đến đúng đối tượng khách hàng, chăm sóc và làm hài lòng khách hàng
        ''')
    st.write(
        '''
        ##### Yêu cầu đưa ra:
        - Tìm ra giải pháp giúp cải thiện hiệu quả quảng bá, từ đó giúp tăng doanh thu bán hàng, cải thiện mức độ hài lòng của khách hàng.
        ''')
    st.write(
        '''
        ##### Mục tiêu/ vấn đề:
        - Xây dựng hệ thống phân nhóm khách hàng dựa trên các thông tin do cửa hàng cung cấp từ đó có thể giúp cửa hàng xác định các nhóm khách hàng khác nhau để có chiến lược kinh doanh, chăm sóc khách hàng phù hợp
        ''')   
    
# -----------------------------------------------------------------------------------
def get_list_customers(df):
    unique_customers = df['Member_number'].unique()
    columns = ['Member_number']
    
    return pd.DataFrame(unique_customers,columns=columns)      
  
# -----------------------------------------------------------------------------------
def create_cluster_name(df,df_name,model):    
    df["Cluster"]=model.predict(df)
    df_new=pd.merge(df,df_name[['ClusterName']],left_on='Cluster',right_index=True,how='inner')
    return df_new

# -----------------------------------------------------------------------------------
def format_RFM(st,df,occupation,visitor=False):
    ClusterName=df['ClusterName'].iloc[0]
    Recency=df['Recency'].iloc[0]
    Frequency=df['Frequency'].iloc[0]
    Monetary=df['Monetary'].iloc[0]

    if visitor:
        st.markdown(f"<h4 style='text-align: center; color:'>🎉Khách hàng đã được phân vào nhóm:</h4>", unsafe_allow_html=True)                    
        st.markdown(f"<h3 style='text-align: center; color: #FF4B4B'>{ClusterName}</h3>", unsafe_allow_html=True)       

        col1,col2,col3=st.columns(3)     
        with col1:
            st.write('')
            st.write('')
            st.markdown(
                f"""
                <div style='text-align: center;'>
                    <span style='display: block; font-size: 40px;'>📅</span>  <!-- Icon -->
                    <span style='display: block; font-size: 25px;color: #00A6ED'>Recency<br>{Recency}</span>  <!-- Text -->
                </div>
                """,
                unsafe_allow_html=True
            )                          
        with col2:
            st.write('')
            st.write('')
            st.markdown(
                f"""
                <div style='text-align: center;'>
                    <span style='display: block; font-size: 40px;'>🔁</span>  <!-- Icon -->
                    <span style='display: block; font-size: 25px;color: #00A6ED'>Frequency<br>{Frequency}</span>  <!-- Text -->
                </div>
                """,
                unsafe_allow_html=True
            )                  
        with col3:
            st.write('')
            st.write('')
            st.markdown(
                f"""
                <div style='text-align: center;'>
                    <span style='display: block; font-size: 40px;'>💴</span>  <!-- Icon -->
                    <span style='display: block; font-size: 25px;color: #00A6ED'>Monetary<br>{Monetary}</span>  <!-- Text -->
                </div>
                """,
                unsafe_allow_html=True
            )                   
    else:       
        st.markdown(f"<h4 style='text-align: center; color:'>🎉Khách hàng id=<span style='color: #29B09D;'>{occupation}</span> đã được phân vào nhóm:</h4>", unsafe_allow_html=True)                    
        st.markdown(f"<h3 style='text-align: center; color: #FF4B4B'>{ClusterName}</h3>", unsafe_allow_html=True)     
          
        amount=df['amount'].iloc[0] 

        col1,col2,col3,col4=st.columns(4)  
        with col1:
            st.write('')
            st.write('')
            st.markdown(
                f"""
                <div style='text-align: center;'>
                    <span style='display: block; font-size: 40px;'>📅</span>  <!-- Icon -->
                    <span style='display: block; font-size: 25px;color: #00A6ED'>Recency<br>{Recency}</span>  <!-- Text -->
                </div>
                """,
                unsafe_allow_html=True
            )                          
        with col2:
            st.write('')
            st.write('')
            st.markdown(
                f"""
                <div style='text-align: center;'>
                    <span style='display: block; font-size: 40px;'>🔁</span>  <!-- Icon -->
                    <span style='display: block; font-size: 25px;color: #00A6ED'>Frequency<br>{Frequency}</span>  <!-- Text -->
                </div>
                """,
                unsafe_allow_html=True
            )                  
        with col3:
            st.write('')
            st.write('')
            st.markdown(
                f"""
                <div style='text-align: center;'>
                    <span style='display: block; font-size: 40px;'>💴</span>  <!-- Icon -->
                    <span style='display: block; font-size: 25px;color: #00A6ED'>Monetary<br>{Monetary}</span>  <!-- Text -->
                </div>
                """,
                unsafe_allow_html=True
            )                  
        with col4:
            st.write('')
            st.write('')
            st.markdown(
                f"""
                <div style='text-align: center;'>
                    <span style='display: block; font-size: 40px'>🛒</span>  <!-- Icon -->
                    <span style='display: block; font-size: 25px;color: #00A6ED'>Amount<br>{round(amount,2)}</span>  <!-- Text -->
                </div>
                """,
                unsafe_allow_html=True
            ) 

# -----------------------------------------------------------------------------------
def select_one_customers_by_id(customer_id_list,df,st):
    options = ['']+customer_id_list['Member_number'].tolist()
    occupation = st.selectbox('Chọn khách hàng theo id (Member_number):',options,
        format_func=lambda x: 'Chọn một khách hàng' if x == '' else x,
    )

    if occupation!='':
        st.write("Khách hàng được chọn:", occupation)
        selected_cus=df[df['Member_number']==occupation]
        if not selected_cus.empty:
            selected_cus=selected_cus.groupby(['ClusterName','Recency','Frequency','Monetary']).agg({'amount':'sum'})
            selected_cus.reset_index(inplace=True)
            format_RFM(st=st,df=selected_cus,occupation=occupation,visitor=False)                
            st.write('')
            st.divider()
            giai_thich_ClusterName(st,selected_cus['ClusterName'].iloc[0])

# -----------------------------------------------------------------------------------
def select_one_customers_by_RFM(df,df_name,model,st):
    recency_min=df['Recency'].min()
    recency_max=df['Recency'].max()
    frequency_min=df['Frequency'].min()
    frequency_max=df['Frequency'].max()
    monetary_min=float(df['Monetary'].min())
    monetary_max=float(df['Monetary'].max())

    seg=5
    R = st.slider("Recency", recency_min, recency_max, int((recency_max-recency_min)/seg))
    st.write("Recency: ", R)

    F = st.slider("Frequency", frequency_min, frequency_max, int((frequency_max-frequency_min)/seg))
    st.write("Frequency: ", F)

    M_ = st.slider("Monetary", monetary_min, monetary_max, (monetary_max-monetary_min)/seg, 0.1)
    # Tạo number_input để điều chỉnh giá trị chi tiết hơn
    M = st.number_input("Nhập giá trị chính xác:", min_value=monetary_min, max_value=monetary_max, value=M_, step=0.1, format="%.1f")  # Điều chỉnh step và format theo nhu cầu
    M=round(M,1)
    st.write("Monetary:", M)

    cols=['Recency','Frequency','Monetary']
    df_new=pd.DataFrame([[R,F,M]],columns=cols)
    df_new=create_cluster_name(df_new,df_name,model)
    format_RFM(st,df_new,-1,True)
    st.write('')
    st.divider()
    giai_thich_ClusterName(st,df_new['ClusterName'].iloc[0])

# -----------------------------------------------------------------------------------    
def download_file(st,file_path):
    with open(file_path, "r") as file:
        csv_data = file.read()
    st.download_button(
        label="Tải xuống tệp CSV mẫu",
        data=csv_data,
        file_name="file_mau.csv",
        mime="text/csv"
    )

# -----------------------------------------------------------------------------------            
def upload_customers_file(st,model,df_name):
    file = st.file_uploader("Chọn file", type=["csv", "txt"])

    if file is not None:
        df_cus_file = pd.read_csv(file)     
        df_cus_file=df_cus_file.set_index('Member_number') 
        st.write('#### Nội dung file upload')  
        st.markdown(format_table(df_cus_file).to_html(), unsafe_allow_html=True)        
        submitted = st.button("Thực hiện phân nhóm")
        if submitted:
            df_cus_file=create_cluster_name(df_cus_file,df_name,model)
            df_cus_file=df_cus_file.reset_index()
            st.subheader('Bảng phân nhóm danh sách khách hàng 🎉')
            st.markdown(format_table(df_cus_file).to_html(), unsafe_allow_html=True)
    else:
        st.write("Vui lòng chọn file.")   

# -----------------------------------------------------------------------------------
def get_top_products_cluster_info(df, top_n=3):
  top_products_per_cluster = df.groupby(['ClusterName', 'productName'])['items'].sum().reset_index().sort_values(['ClusterName', 'items'], ascending=[True, False]).groupby('ClusterName').head(top_n)
  top_category_per_cluster = df.groupby(['ClusterName', 'Category'])['items'].sum().reset_index().sort_values(['ClusterName', 'items'], ascending=[True, False]).groupby('ClusterName').head(top_n)
  top_products_amount_per_cluster = df.groupby(['ClusterName', 'productName'])['amount'].sum().reset_index().sort_values(['ClusterName', 'amount'], ascending=[True, False]).groupby('ClusterName').head(top_n)
  return top_products_per_cluster, top_category_per_cluster, top_products_amount_per_cluster 

# -----------------------------------------------------------------------------------
def draw_top_products_cluster_info(y, ylabel, hue, title, legend_title, data):
    fig = px.bar(
        data,
        x="ClusterName",
        y=y,
        color=hue,
        title=title,
        labels={y: ylabel, hue: legend_title},
        color_discrete_sequence=px.colors.qualitative.Pastel, 
    )

    fig.update_layout(
        xaxis_title="Cluster Name",
        yaxis_title=ylabel,
        font=dict(size=12),
        xaxis_tickangle=-45,
        title_font=dict(size=16, weight="bold"),
    )

    # Hiển thị giá trị trên mỗi cột
    fig.update_traces(texttemplate='%{y:.0f}', textposition='outside')

    return fig

# -----------------------------------------------------------------------------------
def truc_quan_hoa_treemap(rfm_agg,modelName):        
    cluster_name='ClusterName'
    if modelName =='Tập luật':
        cluster_name='RFM_Level'

    df_rfm_agg=rfm_agg.copy()
    df_rfm_agg[cluster_name+'Upper']=df_rfm_agg[cluster_name].str.upper()
    fig = px.treemap(
        df_rfm_agg,
        path=[cluster_name+'Upper'],
        values='Count',
        color=cluster_name,
        hover_data=['RecencyMean', 'FrequencyMean', 'MonetaryMean', 'Percent'],
        title=f"RFM Clustering with {modelName} (tree map)"
    )

    fig.update_traces(
        textinfo="label+value+percent root", 
        texttemplate='%{label}<br><br>%{customdata[0]} days<br>%{customdata[1]} orders<br>%{customdata[2]:.2f} $<br>%{value} customers (%{customdata[3]:.2f} %)',
        customdata=df_rfm_agg[['RecencyMean', 'FrequencyMean','MonetaryMean','Percent']],
        textfont={'size': 12} 
        # textfont={'size': 14, 'family': 'Arial', 'color': 'black', 'weight': 'bold'} 
        )
    
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    return fig


# -----------------------------------------------------------------------------------
def truc_quan_hoa_scatter(rfm_agg,modelName):
    cluster_name='ClusterName'
    if modelName =='Tập luật':
        cluster_name='RFM_Level'    

    fig = px.scatter(rfm_agg, x="RecencyMean", y="MonetaryMean", size="FrequencyMean", color=cluster_name,
           hover_name=cluster_name, size_max=50,opacity=0.7)
    fig.update_layout(title=f'RFM Clustering with {modelName} (bubble chart)')
    return fig

# -----------------------------------------------------------------------------------
def truc_quan_hoa_scatter_3d_avg(rfm_agg,modelName):
    cluster_name='ClusterName'
    if modelName =='Tập luật':
        cluster_name='RFM_Level'

    fig = px.scatter_3d(rfm_agg, x='RecencyMean', y='FrequencyMean', z='MonetaryMean',
                        size="FrequencyMean",
                        color=cluster_name, size_max=70, opacity=0.7)
    fig.update_layout(title=f'RFM Clustering with {modelName} (bubble chart 3d)',
                    scene=dict(xaxis_title='Recency',
                                yaxis_title='Frequency',
                                zaxis_title='Monetary'))
    return fig 


# -----------------------------------------------------------------------------------
def truc_quan_hoa_scatter_3d_data(df,modelName):
    cluster_name='ClusterName'
    if modelName =='Tập luật':
        cluster_name='RFM_Level'        

    fig = px.scatter_3d(df, x='Recency', y='Frequency', z='Monetary',
                        color=cluster_name, size_max=10, opacity=0.7)
    fig.update_layout(title=f'RFM Clustering with {modelName} (scatter plot)',
                    scene=dict(xaxis_title='Recency',
                                yaxis_title='Frequency',
                                zaxis_title='Monetary'))
    return fig  

def ve_cac_bieu_do(rfm_agg,df,st,modelName):
    fig_treemap=truc_quan_hoa_treemap(rfm_agg,modelName)
    st.write("")
    st.plotly_chart(fig_treemap)

    fig_scatter=truc_quan_hoa_scatter(rfm_agg,modelName)
    st.write("")
    st.plotly_chart(fig_scatter)

    fig_scatter_3d_avg=truc_quan_hoa_scatter_3d_avg(rfm_agg,modelName)
    st.write("")
    st.plotly_chart(fig_scatter_3d_avg)

    fig_scatter_3d_data=truc_quan_hoa_scatter_3d_data(df,modelName)
    st.write("")
    st.plotly_chart(fig_scatter_3d_data) 

# ===================================================================================
if __name__ == "__main__":
    pass
