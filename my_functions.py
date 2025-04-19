import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

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
def format_table(df):
    df_new=df.copy()
    if 'Monetary' in df.columns:
        df_new['Monetary']=df_new['Monetary'].map(lambda x: f'{x:.1f}')

    styler = df_new.style.set_table_styles(
        [
            {'selector': 'th', 'props': [('text-align', 'center')]},  # Canh phải tiêu đề cột
            {'selector': 'td', 'props': [('text-align', 'center')]},  # Canh giữa nội dung
            {'selector': 'th:first-child', 'props': [('background-color', 'lightblue')]},  # Nền xanh nhạt cho tiêu đề cột đầu tiên
        ]    
    )
    return styler    
    
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
def format_RFM(st,df,occupation,recent_values,max_values,ranges,visitor=False):
    ClusterName=df['ClusterName'].iloc[0]
    Recency=df['Recency'].iloc[0]
    Frequency=df['Frequency'].iloc[0]
    Monetary=df['Monetary'].iloc[0]

    if visitor:
        st.markdown(f"<h5 style='text-align: center; color:'>🎉Khách hàng đã được phân vào nhóm:</h5>", unsafe_allow_html=True)                    
        st.markdown(f"<h4 style='text-align: center; color: #FF4B4B'>{ClusterName}</h4>", unsafe_allow_html=True)    
    else:
        st.markdown(f"<h5 style='text-align: center; color:'>🎉Khách hàng id=<span style='color: #29B09D;'>{occupation}</span> đã được phân vào nhóm:</h5>", unsafe_allow_html=True)                    
        st.markdown(f"<h4 style='text-align: center; color: #FF4B4B'>{ClusterName}</h4>", unsafe_allow_html=True)  

    col1,col2,col3=st.columns(3)     
    with col1:  
        st.markdown(
            f"""
            <div style='text-align: center;'>
                <span style='display: block; font-size: 35px;'>📅</span>  <!-- Icon -->
                <span style='display: block; font-size: 20px;color: #00A6ED'>Recency<br>{Recency}</span>  <!-- Text -->
            </div>
            """,
            unsafe_allow_html=True
        ) 
        fig_gauge_chart=gauge_chart(recent_values[0],max_values[0],ranges[0],'Recency')
        st.plotly_chart(fig_gauge_chart)                                 
    with col2:   
        st.markdown(
            f"""
            <div style='text-align: center;'>
                <span style='display: block; font-size: 35px;'>🔁</span>  <!-- Icon -->
                <span style='display: block; font-size: 20px;color: #00A6ED'>Frequency<br>{Frequency}</span>  <!-- Text -->
            </div>
            """,
            unsafe_allow_html=True
        ) 
        fig_gauge_chart=gauge_chart(recent_values[1],max_values[1],ranges[1],'Frequency')
        st.plotly_chart(fig_gauge_chart)                        
    with col3:   
        st.markdown(
            f"""
            <div style='text-align: center;'>
                <span style='display: block; font-size: 35px;'>💴</span>  <!-- Icon -->
                <span style='display: block; font-size: 20px;color: #00A6ED'>Monetary<br>{Monetary}</span>  <!-- Text -->
            </div>
            """,
            unsafe_allow_html=True
        )    
        fig_gauge_chart=gauge_chart(recent_values[2],max_values[2],ranges[2],'Monetary')
        st.plotly_chart(fig_gauge_chart)   

# -----------------------------------------------------------------------------------        
def format_RFM_2(st,df):
    css_string = """
        <style>
        .centered-content {
            text-align: center;
        }
        .centered-content span {
            display: block;
        }
        .centered-content .icon {
            font-size: 40px; 
        }
        .centered-content .text {
            font-size: 15px;
            color: #264653;
            background-color: #ADD8E6;
            border-radius: 10px; /* Bo tròn góc 8px */
        }      
        /* Selector CSS cụ thể hơn cho cột */
        div[data-testid="stVerticalBlock"] .centered-content .icon { 
            font-size: 40px !important; 
        }
        div[data-testid="stVerticalBlock"] .centered-content .text {
            font-size: 15px !important;
        }
        </style>
    """   

    col1,col2,col3,col4=st.columns(4)
    with col1:
        html_string1 = f"""
        <div class="centered-content">      
            <span class="icon">👨‍👩‍👧‍👦</span>  <!-- Icon -->     
            <span class="text">Số Khách hàng: <span style="font-weight: bold; font-size: 25px;color: #EB685E;">{df['Member_number'].nunique()}</span><br>Số Cluster: <span style="font-weight: bold; font-size: 25px;color: #EB685E;">{df['ClusterName'].nunique()}</span></span>  <!-- Text -->                               
        </div>
        """
        final_html = css_string + html_string1
        st.markdown(final_html, unsafe_allow_html=True)
       
    with col2:    
        html_string2 = f"""
        <div class="centered-content">      
            <span class="icon">📅</span>  <!-- Icon -->     
            <span class="text">Recency min: <span style="font-weight: bold; font-size: 25px;color: #EB685E;">{df['Recency'].min()}</span><br>Recency max: <span style="font-weight: bold; font-size: 25px;color: #EB685E;">{df['Recency'].max()}</span></span>  <!-- Text -->                 
        </div>
        """
        final_html = css_string + html_string2
        st.markdown(final_html, unsafe_allow_html=True)
    with col3:
        html_string3 = f"""
        <div class="centered-content">      
            <span class="icon">🔁</span>  <!-- Icon -->     
            <span class="text">Frequency min: <span style="font-weight: bold; font-size: 25px;color: #EB685E;">{df['Frequency'].min()}</span><br>Frequency max: <span style="font-weight: bold; font-size: 25px;color: #EB685E;">{df['Frequency'].max()}</span></span>  <!-- Text -->                 
        </div>
        """
        final_html = css_string + html_string3
        st.markdown(final_html, unsafe_allow_html=True)        
    with col4:
        # display: inline-block;
        html_string4 = f"""
        <div class="centered-content">      
            <span class="icon">💴</span>  <!-- Icon -->     
            <span class="text">Monetary min: <span style="font-weight: bold; font-size: 25px;color: #EB685E;">{df['Monetary'].min()}</span><br>Monetary max: <span style="font-weight: bold; font-size: 25px;color: #EB685E;">{df['Monetary'].max()}</span></span>  <!-- Text -->                 
        </div>
        """
        final_html = css_string + html_string4
        st.markdown(final_html, unsafe_allow_html=True)      

    # st.markdown('<br>', unsafe_allow_html=True)
    # --------------------------------------------------
    cluster_counts = df['ClusterName'].value_counts()
    df_cluster_ratios = pd.DataFrame({'ClusterName': cluster_counts.index, 'Ratio': cluster_counts.values / cluster_counts.sum()})
    fig = px.pie(df_cluster_ratios, values='Ratio', names='ClusterName', title='Tỷ lệ các Cluster')
    fig.update_layout(title_font_size=20)  # Tăng kích thước tiêu đề
    fig.update_layout(legend=dict(font=dict(size=22)))  # Tăng kích thước chữ legend
    fig.update_layout(height=400, width=500)  # Thiết lập kích thước tại đây
    st.plotly_chart(fig)

    selected_option= 'Giải thích Cluster'
    if selected_option:
        # Tạo key duy nhất cho session_state dựa trên selected_option
        expander_key = f"expander_state_{selected_option}"

        # Khởi tạo trạng thái expander là True khi selectbox được chọn
        if expander_key not in st.session_state:
            st.session_state[expander_key] = False  # Mặc định đóng expander

        # Hiển thị expander với trạng thái từ session_state
        with st.expander(str(selected_option), expanded=st.session_state[expander_key]):
            for name in df_cluster_ratios['ClusterName']:
                giai_thich_ClusterName(st,name)


    # st.write("##### Danh sách các Cluster:")
    # unique_clusters = df['ClusterName'].unique().tolist()

    # # Chia danh sách thành các nhóm 3 phần tử (3 cột)
    # cluster_groups = [unique_clusters[i:i + 3] for i in range(0, len(unique_clusters), 3)]

    # # Tạo bảng với 2 hàng và 3 cột
    # for row in cluster_groups:
    #     cols = st.columns(len(row))  # Tạo số cột tương ứng với số phần tử trong nhóm
    #     for i, cluster in enumerate(row):
    #         with cols[i]:
    #             st.markdown(f"<h5 style='text-align: left; color: #8D65C5'>{cluster}</h5>", unsafe_allow_html=True)




         
# -----------------------------------------------------------------------------------
def select_one_customers_by_id(customer_id_list,df,st):
    options = ['']+customer_id_list['Member_number'].tolist()
    occupation = st.selectbox('Chọn khách hàng theo id (Member_number):',options,
        format_func=lambda x: 'Chọn một khách hàng' if x == '' else x,
    )

    if occupation!='':        
        # st.write("Khách hàng được chọn:", occupation)
        search_cus=df[df['Member_number']==occupation]
        if not search_cus.empty:
            selected_cus=search_cus.groupby(['ClusterName','Recency','Frequency','Monetary']).agg({'amount':'sum'})
            selected_cus.reset_index(inplace=True)
   
            recent_values=[selected_cus['Recency'].iloc[0],selected_cus['Frequency'].iloc[0],selected_cus['Monetary'].iloc[0]]
            max_values=[df['Recency'].max(),df['Frequency'].max(),df['Monetary'].max()]
            ranges=xac_dinh_pham_vi(df)
            format_RFM(st,selected_cus,occupation,recent_values,max_values,ranges,False)
            # st.write('')

            st.write('**Lịch sử giao dịch của khách hàng:**')
            selected_option= str(occupation)
            if selected_option:
                # Tạo key duy nhất cho session_state dựa trên selected_option
                expander_key = f"expander_state_{selected_option}"

                # Khởi tạo trạng thái expander là True khi selectbox được chọn
                if expander_key not in st.session_state:
                    st.session_state[expander_key] = False  # Mặc định đóng expander

                # Hiển thị expander với trạng thái từ session_state
                with st.expander(str(selected_option), expanded=st.session_state[expander_key]):
                    # st.markdown(format_table(search_cus).to_html(), unsafe_allow_html=True)
                    search_cus=search_cus[['Member_number','Date','items','productName','Category','price','amount']].sort_values(by=['Date'])           
                    search_cus.rename(columns={'Member_number':'Member_no'},inplace=True)
                    search_cus.rename(columns={'items':'quantity'},inplace=True)
                    st.dataframe(search_cus, hide_index=True)


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
    M = st.number_input(f"Nhập giá trị chính xác (từ {monetary_min} đến {monetary_max}):", min_value=monetary_min, max_value=monetary_max, value=M_, step=0.1, format="%.1f")  # Điều chỉnh step và format theo nhu cầu
    M=round(M,1)
    st.write("Monetary:", M)

    cols=['Recency','Frequency','Monetary']
    df_new=pd.DataFrame([[R,F,M]],columns=cols)
    df_new=create_cluster_name(df_new,df_name,model)

    recent_values=[df_new['Recency'].iloc[0],df_new['Frequency'].iloc[0],df_new['Monetary'].iloc[0]]
    max_values=[df['Recency'].max(),df['Frequency'].max(),df['Monetary'].max()]
    ranges=xac_dinh_pham_vi(df)
    format_RFM(st,df_new,-1,recent_values,max_values,ranges,True)
    st.write('')
    st.divider()
    giai_thich_ClusterName(st,df_new['ClusterName'].iloc[0])

# ----------------------------------------------------------------------------------- 
def xac_dinh_pham_vi(df):
    # Xác định các phạm vi
    ranges = [
        [
            (0, df['Recency'].max() * 0.33, "#32CD32"),     # Từ 0 đến 33% (Tốt) (Lime Green)
            (df['Recency'].max() * 0.33, df['Recency'].max() * 0.66, "#FFD700"),  # Từ 33% đến 66% (Trung bình) (Gold)
            (df['Recency'].max() * 0.66, float(df['Recency'].max()), "#FF6347")   # Từ 66% đến 100% (Kém) (Tomato)
        ],
        [
            (0, df['Frequency'].max() * 0.33, "#FF6347"),     # Từ 0 đến 33% (Kém) (Tomato)
            (df['Frequency'].max() * 0.33, df['Frequency'].max() * 0.66, "#FFD700"),  # Từ 33% đến 66% (Trung bình) (Gold)
            (df['Frequency'].max() * 0.66, float(df['Frequency'].max()), "#32CD32")   # Từ 66% đến 100% (Tốt) (Lime Green)
        ],
        [
            (0, df['Monetary'].max() * 0.33, "#FF6347"),     # Từ 0 đến 33% (Kém) (Tomato)
            (df['Monetary'].max() * 0.33, df['Monetary'].max() * 0.66, "#FFD700"),  # Từ 33% đến 66% (Trung bình) (Gold)
            (df['Monetary'].max() * 0.66, float(df['Monetary'].max()), "#32CD32")   # Từ 66% đến 100% (Tốt) (Lime Green) 
        ]]   
    return ranges

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
        st.write(df_cus_file)     

        submitted = st.button("Thực hiện phân nhóm")
        if submitted:
            df_cus_file=create_cluster_name(df_cus_file,df_name,model)
            df_cus_file=df_cus_file.reset_index()   
            st.subheader('Bảng phân nhóm danh sách khách hàng 🎉')
            st.markdown(format_table(df_cus_file).to_html(), unsafe_allow_html=True)
            format_RFM_2(st,df_cus_file)
    else:
        st.write("Vui lòng chọn file.")   

# -----------------------------------------------------------------------------------
# Tạo callback function cho sự kiện click
def on_click(st,row_index):
    st.session_state.selected_row = row_index
    st.experimental_rerun()        

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
def so_sanh_cac_thuat_toan(st,df):
    tieu_de=df.columns
    html_style="""
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                word-wrap: break-word; /* Cho phép text tự động xuống dòng */
                white-space: normal; /* Giúp chữ không bị tràn ra ngoài */
            }
            th {
                background-color: #f2f2f2;
                text-align: left;
            }
        </style>
        """
    # Tạo bảng HTML từ dữ liệu
    html_table = "<table border='1' style='width:100%; text-align:left;'>"
    html_table += f"<tr><th>{tieu_de[0]}</th><th>{tieu_de[1]}</th><th>{tieu_de[2]}</th><th>{tieu_de[3]}</th></tr>"
    for itr,row in df.iterrows():
        html_table += f"<tr><td>{row['Thuật toán']}</td><td>{row['Nguyên lý']}</td><td>{row['Ưu điểm']}</td><td>{row['Nhược điểm']}</td></tr>"
    html_table += "</table>"

    # Hiển thị bảng
    st.markdown(html_style + html_table, unsafe_allow_html=True)    



# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------
def plot_distribution(st,data, title, xlabel):
    col1,col2=st.columns(2)
    with col1:
        fig1, ax1 = plt.subplots(figsize=(8, 4),dpi=300) # Điều chỉnh kích thước biểu đồ
        sns.histplot(data, ax=ax1, bins=20, kde=True) # Optional: kde=True for density curve
        ax1.set_title(title, fontsize=14) # Điều chỉnh kích thước font chữ
        ax1.set_xlabel(xlabel, fontsize=12)
        ax1.set_ylabel("Số lượng", fontsize=12)
        st.pyplot(fig1)
    with col2:
        fig2, ax2 =plt.subplots(figsize=(8, 4),dpi=300)
        sns.boxplot(data=data, ax=ax2,x=xlabel)
        ax2.set_title(title, fontsize=14) # Điều chỉnh kích thước font chữ
        ax2.set_xlabel(xlabel, fontsize=12)
        # ax2.set_ylabel("Số lượng", fontsize=12)        
        plt.title(f'Boxplot của {xlabel}')       
        st.pyplot(fig2)

# -----------------------------------------------------------------------------------
def gauge_chart(value,max_values,ranges,name):  
    steps=[]
    for range in ranges:
        step={'range': [range[0],range[1]],'color':range[2]}
        steps.append(step)

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,  # Giá trị hiện tại
        domain={'x': [0, 1], 'y': [0, 1]},  # Vị trí biểu đồ
        title={"text":f"{name} max: {max_values}","font":{"size": 17}},
        gauge={
            'axis': {'range': [None, max_values]},  # Phạm vi từ 0 đến max
            'bar': {'color': "blue"},  # Thanh giá trị màu đen
            'steps':steps
        }
    ))

    # Tùy chỉnh chiều cao và rộng của biểu đồ
    fig.update_layout(
        height=150,  # Điều chỉnh chiều cao
        margin=dict(t=0, b=0, l=50, r=50)  # Giảm khoảng cách thừa  
        )  

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
